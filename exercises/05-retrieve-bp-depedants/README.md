# Exercise 05 - Retrieve Business Partner dependant's information

At the end of this exercise, you'll have successfully retrieved Business Partner dependant data hosted in the European instance of the BP Dependants service.

![Connect the integration flow to the European instance of the BP Dependants service](assets/diagrams/bp_data_flow.png)
<p align = "center">
<i>Exercise 05 - Data flow</i>
</p>

Now that we are familiar with the basics of SAP Cloud Integration, we will start moving a bit faster when adding components and deploying the integration flow. When we finish the exercise our integration flow will include a few additional Content Modifiers and we will have implemented a new pattern - Router (Content Based Routing)[^1].

![Integration flow - End of Exercise 05](assets/end-of-exercise-integration-flow.png)
<p align = "center">
<i>Integration Flow - End of Exercise 05</i>
</p>

## Design

👉 Let's start by making a copy of the integration flow we created in Exercise 03, add the `- Exercise 05` suffix to the name and open it.

![Connect the integration flow to the European instance of the BP Dependants service](assets/copy-integration-flow.gif)

We create a copy of the integration flow to keep the past version as a reference. This will help you revisit the integration flow when reviewing the content or trying to remember what you've developed as part of the CodeJam.

To keep things simple we will only process data for European countries in this exercise. The integration flow needs to know the data of which countries can be served by the EU server. In a real-world scenario, we would not want to have this as a fixed (hard-coded) value in our integration flow. It needs to be easy to tell our integration flow that the data for new countries can be retrieved from a particular server. Ideally, this would be a parameter that we can configure in our integration flow. Enter Externalised Parameters.

### Externalised Parameters

As stated in the [documentation](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/45b2a0772db94bd9b0e57bc82d8d3797.html?locale=en-US), *the Externalize feature allows us to declare a parameter as a variable and reuse it across multiple components in our integration flow*. In our case, we will create an external parameter called `european_countries`, that will contain the details of the countries that we can retrieve from the European instance of the Business Partner Dependants service. So far, we have not defined any external parameters. You can see the external parameters of an integration flow by going to the `Externalized Parameters tab` in the Integration Flow configuration section.

![Integration Flow configuration - Externalized Parameters tab](assets/externalized-parameters-tab.png)
<p align = "center">
<i>Integration Flow configuration - Externalized Parameters tab</i>
</p>

👉 Extend the `Set employee_id property` content modifier to create a new property called `european_countries` which will be assigned the value configured for the external parameter with the same name and set `DE,FR,ES,IT,PT` as the default value. Optional: Rename the content modifier to reflect the additional action, e.g. Set employee_id and country properties.

> Click the **Add button** in the Exchange Property tab, enter `european_countries` as the name and `{{european_countries}}` as source value. The double curly braces indicates to SAP Cloud Integration that this is an external parameter. Click the tab key or change the focus field so that the UI can detect the external parameter. As the external parameter doesn't exist, we need to define a value for it.

![Create european_countries property and external parameter](assets/create-property-with-externalised-parameter.gif)
<p align = "center">
<i>Create european_countries property and external parameter</i>
</p>

### Process the SAP S/4HANA Cloud mock service response

In the previous exercise, we returned the response of the mock service as is to test that our initial communication was working. Let's do some minor processing of the response. 

The response contains the Business Partner details. In it, we can find the `to_BusinessPartnerAddress` field. This field contains an array of addresses associated with the employee. In our case, we can know where an employee is located based on the first address' `to_BusinessPartnerAddress.results.Country` field. 

```bash
$ echo "Business Partner address: $(jq '.d.to_BusinessPartnerAddress.results[0].Country' exercises/03-build-first-integration-flow/assets/sample-response.json)"
Business Partner address: "DE"
```

We will process the response by first converting the JSON response to XML. Once our payload is in XML format, we can retrieve the Business Partner Address Country using XPath and assign it to a variable. This variable can then be used to define the conditions required to process the request further.

![Process mock service reponse - JSON to XML Converter and Content Modifier](assets/convert-to-xml-and-content-modifier.png)
<p align = "center">
<i>Process mock service reponse - JSON to XML Converter and Content Modifier</i>
</p>

👉 First, add another `JSON to XML converter` after the Request Reply step. Then, add a `Content Modifier` and create a new property called `employee_country`. Given that our payload is in XML format, we can use XPath to retrieve the . Set `/d/to_BusinessPartnerAddress/results/Country` as the XPath.

Our response payload contains a field that we can use as "root node" - `d`. We don't need to add a root node so we can unselect the `Add XML Root Element checkbox` when configuring the converter.

![Convert BP response to XML configuration](assets/converter-configuration.png)
<p align = "center">
<i>Convert BP response to XML configuration</i>
</p>

🔎 Check that your Get Employee Country configuration matches the screenshot below.

![Get Employee Country content modifier configuration](assets/employee-country-exchange-property.png)
<p align = "center">
<i>Get Employee Country content modifier configuration</i>
</p>

Once we set up the steps above, we are ready to route our message using the data available.

### Route the message

We need to direct the message to the correct service instance based on the employee's country. We've stored the `employee_country` in the previous section and we will need to define the conditions based on its value. To achieve this, we can use the [Router component](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/d7fddbd52e3944d3a6d4e5b228c7e63b.html?locale=en-US) and set different conditions depending on the route.

To keep things simple we will only send requests to the european instance of the Business Partner Dependants mock service. Therefore, we will only define two routes for our router:
- Default route (*Receiver not found*): This will be the route taken when no receiver is found. A receiver will not be found when the employee's country is not a European country, e.g. US. Here we will handle an error scenario. 
- European route (*Route to EU*): Proceed to call the european instance.

![Add router and content modifier in default route](assets/add-router-and-content-modifier-in-default-route.png)
<p align = "center">
<i>Add router and content modifier in default route</i>
</p>

👉 First, add a `Router` step right after the `Get Employee Country` content modifier we added in the previous section. Then, add the two routes below. *Note: To define the condition/settings of a route, you need to select the connection (→) between the router and the target step.*
1.  *Route to EU*: Connect it to the existing `End Message event` and define as its condition the following:
    - Expression Type: `Non-XML`
    - Condition: `${property.employee_country} in ${property.european_countries}`. 
    > 🐪 This is a Simple language expression[^2]. We check that a string exists within another string.
2. *Receiver not found*: Connect the Router to a new `End Message event` and within it include a `Content Modifier` step. In the Content Modifier, we create a new message header - `CamelHttpResponseCode` and set the constant 500 as its value. Also, set the Message Body to the payload below.
   ```json
    {
        "error": "Employee's country not supported"
    }
   ```
   > 🐪 The CamelHttpResponseCode message header is documented in the [HTTP Camel Component](https://camel.apache.org/components/3.18.x/http-component.html). We need to set a value for it if we want our integration flow to return a different HTTP code than the default 200 HTTP Code.

Once you've set up the routes, go to the Router's Processing tab and set the Receiver not found as the default route.

![Router - Processing routes](assets/router-rocessing-routes.png)
<p align = "center">
<i>Router - Processing routes</i>
</p>

#### (Optional) Test the routing condition

We've done quite a few things already. We can run a test in our integration flow to ensure that everything is set up correctly. SAP Cloud Integration allow us to test elements (simulate) in our integration flow without the need of deploying the integration flow and sending a request from an external client. Using [Simulation](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/45a71f8ffd74436aaf02a3536f3c6992.html?locale=en-US) we can speed up our development process and quickly validate that our conditions are working as expected. Let's simulate that we've received the response from the SAP S/4HANA Cloud system and test our routing condition. 

![Set up simulation in integration flow](assets/set-up-simulation.gif)
<p align = "center">
<i>Set up simulation in integration flow</i>
</p>

Below, are the steps that you need to carry out to run a simulation:
- Add a simulation start point
- Add a simulation end point
- Define the headers, properties, body of our message
  - Property: `european_countries` = `DE,FR,ES,IT,PT`
  - Body: Import [`sample_response.json` file](../03-build-first-integration-flow/assets/sample-response.json)
- Run the simulation

#### Deploy API Key to SAP Cloud Integration

We need to include an API key in the request we send to the EU instance of the Business Partner Dependants mock service. We can use the secure store in SAP Cloud Integration to securely store the API key.

👉 First, copy the API Key that's included in the `BP-Dependants-EU` Postman environment. Then, go to `Monitor > Security Material`, create a Secure Parameter and deploy it

![Deploy API key as secure parameter](assets/deploy-secure-parameter.png)
<p align = "center">
<i>Deploy API key as secure parameter</i>
</p>


### Call the European instance of the Business Partner Dependants mock service

Now that we've defined our routing conditions, we can simply call the Business Partner Dependants mock service and return the response to the sender.

#### Deploy 

> 🔐 ⛔️ Alternatively, we could have used the Content Modifier step to add a header with our apiKey but this goes against security best practices 

👉 In the `Route to EU` route, add a Content Modifier step, followed by a 

## Deploy

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 


## Summary

Now that you are familiar with the basic functionality of SAP API Business Hub and the Business Partner API, we are ready to start interacting with the services from which our integration will be extracting data.

## Further reading

* [Link 1](https://blogs.sap.com/)
* [Link 2](https://blogs.sap.com/)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. First question.
2. Second question.

[^1]: Pattern Content Based Routing: https://api.sap.com/integrationflow/Pattern_ContentBasedRouting_IgnoreIfNoReceiver
[^2]: Simple: https://camel.apache.org/components/3.18.x/languages/simple-language.html 