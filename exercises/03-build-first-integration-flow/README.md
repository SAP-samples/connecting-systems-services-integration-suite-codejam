# Exercise 03 - Building our first integration flow

At the end of this exercise, you'll have successfully created a simple integration flow that communicates with the SAP S/4HANA Cloud mock server.

> **What is an integration flow [^1]?** 
> 
> An integration flow allows you to specify how SAP Cloud Integration is to process a message. The modeling environment, provided in SAP Cloud Integration, allows you to design the details of message processing (its senders and receivers as well as the individual processing steps) with a graphical user interface.

The diagram below captures, from a data flow point of view, what we are going to achieve as part of this exercise. We will expose an HTTP endpoint through which we will be able to send requests to the integration flow we develop. The integration flow will extract some data (the employee_id) from the payload received, which will then be used to retrieve the Business Partner information from the SAP S/4HANA Cloud mock server. 

![Data flow](assets/diagrams/first_data_flow.png)

The integration flow expects a sample request message like the one below and it should return a response message like the one underneath the request. 

> A full sample response payload can be found in the assets folder - [sample-response.json](assets/sample-response.json)

```json
// Sample request
{
    "employee_id": "1003764"
}

// Sample response
{
    "d": {
        "__metadata": {
            "id": "http://s4-mock-server-service.default.svc.cluster.local:443/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner('1003764')",
            "uri": "http://s4-mock-server-service.default.svc.cluster.local:443/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner('1003764')",
            "type": "API_BUSINESS_PARTNER.A_BusinessPartnerType"
        },
        "BusinessPartner": "1003764",
        "Customer": "",
        "Supplier": "",
        "AcademicTitle": "",
        "AuthorizationGroup": "",
        "BusinessPartnerCategory": "1",
        "BusinessPartnerFullName": "John Doe",
        "BusinessPartnerGrouping": "BP02",
        "BusinessPartnerName": "John Doe",
        "BusinessPartnerUUID": "00163e30-4e2a-1ed8-8483-a08c52249f04",
        ...
        "to_BusinessPartnerAddress": {
            "results": [
                {
                    "__metadata": {
                        "id": "http://s4-mock-server-service.default.svc.cluster.local:443/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartnerAddress(BusinessPartner='1003764',AddressID='28238')",
                        "uri": "http://s4-mock-server-service.default.svc.cluster.local:443/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartnerAddress(BusinessPartner='1003764',AddressID='28238')",
                        "type": "API_BUSINESS_PARTNER.A_BusinessPartnerAddressType"
                    },
                    "BusinessPartner": "1003764",
                    "AddressID": "28238",
                    "ValidityStartDate": "/Date(1518393600000+0000)/",
                    "ValidityEndDate": "/Date(253402300799000+0000)/",
                    "AuthorizationGroup": "",
                    "AddressUUID": "00163e30-4e2a-1ed8-8483-a08c5224bf04",
                    "AdditionalStreetPrefixName": "",
                    "AdditionalStreetSuffixName": "",
                    "AddressTimeZone": "CET",
                    "CareOfName": "",
                    "CityCode": "",
                    "CityName": "Walldorf",
                    "CompanyPostalCode": "",
                    "Country": "DE",
                    "County": "",
                    "DeliveryServiceNumber": "",
                    "DeliveryServiceTypeCode": "",
                    ...
                }
            ]
        }
    }
}
```


## Access your Cloud Integration workspace

You set up SAP Integration Suite and activated several capabilities as part of the prerequisites of this SAP CodeJam. We now need to access the Cloud Integration workspace to start building our first integration flow.

👉 Go to the BTP Cockpit and open the SAP Integration Suite application from within Services > Instances and Subscriptions and then choose the *Design, Develop, and Operate Integration Scenarios* tile.

![Accessing SAP Cloud Integration](assets/accessing-cloud-integration.gif)

We are now in the landing page of SAP Cloud Integration. The page is divided in the following sections: Discover, Design, Monitor, and Settings. We will be interacting the most with Design and Monitor. Below a brief explanation on what you can find in each section.

![Cloud Integration landing page](assets/cloud_integration_landing_page.png)

- Discover: Here, you can find predefined integration content provided by SAP that you can use out of the box and adapt to your requirements.
- Design: This is where you design your integration content. It contains the graphical integration flow modeling environment. You find a list of integration packages defined for the tenant. When you select an integration package, you can find the integration flows (and other artifacts) defined for the package (on the Artifacts tab).
- Monitor: This is where you can monitor your integration flow. You also use this section to manage additional artifacts that you need to deploy on your tenant to complement your integration flows (for example, User Credential artifacts to configure connections using basic authentication).


## Design

Let's jump to the Design section to start developing our integration flow. Before designing our integration flow, we will need to create an integration package. Cloud Integration allows us to assemble integration contents, e.g. integration flows, message mappings, value mappings, scripts, APIs, into packages so that they can be used in our integration scenarios.

![Design section](assets/design-section.png)

👉 Click the Create button and enter a name and short description for the integration package.

| Field               | Value                                                            |
| ------------------- | ---------------------------------------------------------------- |
| *Name*              | Connecting Systems CodeJam                                       |
| *Technical Name*    | ConnectingSystemsCodeJam                                         |
| *Short description* | The benefits platform will send us a request for an employee ID. |

![Create Integration Package](assets/create-integration-package.gif)

Once created, we can start adding artifacts to our package. 

👉 Navigate to the `Artifacts` tab in your integration package, Add an Integration Flow, specify a Name and ID for the integration flow. Once created, click on the new integration flow.

| Field  | Value                       |
| ------ | --------------------------- |
| *Name* | Request Employee Dependants |
| *ID*   | RequestEmployeeDependants   |

> If the `Add button` is greyed out it means you are not in Edit mode. Click the `Edit button` in the upper right hand corner.

![Add artifact to package](assets/add-artifact.png)

When accessing the newly created integration flow you'll notice a couple of things:

![New integration flow](assets/new-integration-flow.png)
- There is no connection between the Sender participant and our integration process or the integration process and the Receiver participant.
- The palette is greyed out (*highlighted in orange*) and we are unable to modify the integration flow. This is because our integration flow is not in edit mode. To switch to edit mode, click the `Edit button` (*highlighted in green*).
- The configuration section, at the bottom of the modeling area, is collapsed. The contents of this section will change depending on the object selected in the modeling area. To expand it, click the `Restore button`.
  ![Expand configuration section](assets/expand-configuration-section.gif)


### Modeling 

We will expose the integration flow via an HTTP endpoint. To send requests to the integration flow we will also require a user with the ESBMessaging.send role. The user we will use should have been created as part of the CodeJam [prerequisites](../../prerequisites.md#create-sap-cloud-integration-runtime-client-credentials).

#### Sender participant

👉 If not in editing mode, click the `Edit button` to enter edit mode in our integration flow and connect the sender participant to the start message event and select HTTPS as the adapter. 

![Connect sender](assets/connect-sender-to-start-message.gif)

👉 Now that we've connected the sender participant, we can proceed to configure the connection of the HTTPS adapter. We need to specify an address, a user role and if the endpoint should be CSRF ([Cross-site request forgery](https://owasp.org/www-community/attacks/csrf)) protected. 

![HTTPS adapter connection settings](assets/http-adapter-connection.png)

#### JSON to XML converter

To extract the data needed from the request, we will first convert the JSON payload to XML. This is to ease the message processing in the integration flow, e.g. take advantage of the XPath in the Content Modifier transformation step. For this, we will need to add a couple of steps in the flow. We can do this by selecting the step from the palette (highlighted in orange a few screenshots above) or by clicking the Add button in the hover menu. *I personally prefer using the hover menu as the search functionality is very handy.* 

👉 Add the JSON to XML converter and the Content Modifier transformation to the integration flow

![hover menu to add steps](assets/add-steps-using-hover-menu.gif)

The JSON to XML converter enables you to transform messages in JSON format to XML format. The body of the exchange will be replaced with an XML payload, similar to the one below, and the XML payload will contain a `root` node. The name of the `root` node can be changed in the JSON to XML Converter - Processing tab.

```xml
<?xml version='1.0' encoding='UTF-8'?>
<root>
    <employee_id>1003764</employee_id>
</root>
```

#### Content Modifier

You can use the content modifier to define local properties for storing additional data during message processing. The content modified can also be use to set header properties that can be included in the HTTP request made to other systems. Also, the header and properties can be further used in connectors and conditions. 

👉 Let's create a property in our exchange. The `employee_id` exchange property will store the employee_id value sent in the request payload. To do this, we need to access the value using XPath. Configure the Content Modifier - Exchange Property as shown in the screenshot below.

| Field          | Value                       |
| -------------- | --------------------------- |
| *Action*       | Request Employee Dependants |
| *Name*         | employee_id                 |
| *Source Type*  | XPath                       |
| *Source Value* | /root/employee_id           |
| *Data Type*    | java.lang.String            |

![Create exchange property](assets/create-employee-id-property.png)

#### Request/Reply

For our integration scenarios we require that our integration flow communicates with the SAP S/4HANA Cloud mock server, to retrieve Business Partner data from it. In this case, we will use the request reply step to connect to the Business Partner mock service.

> In exercise 4 we will further process the data received from the SAP S/4HANA Cloud - Business Partner mock service.

👉 Add a Request Reply external call to call the SAP S/4HANA Cloud - Business Partner mock service, connect it to the Receiver participant, select as a [receiver the HTTP adapter](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/2da452effb764b3bb28f8e0a2f5bd480.html?locale=en-US), and set the connections details in the HTTP adapter.

![Add Request Reply step in iFlow](assets/request-reply-step-in-iflow.png)

HTTP Connection details:
| Field           | Value                                                                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| *Address*       | https://s4-mock-server-service.c-1e90315.kyma.ondemand.com/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner('${property.employee_id}') |
| *Query*         | $expand=to_BusinessPartnerAddress                                                                                                              |
| *Proxy Type*    | Internet                                                                                                                                       |
| *Method*        | GET                                                                                                                                            |
| *Authenticaton* | None                                                                                                                                           |

Let's break down the configuration set in the HTTP adapter:
- Connection Details:
  - Address: URL of the SAP S/4HANA Cloud mock server we're connecting to, e.g., https://s4-mock-server-service.c-1e90315.kyma.ondemand.com. You'll notice that we are also including the full path, and dynamically setting the value stored in the `employee_id` exchange property as part of the URL. 
  - Query: Query string that we want to send with the HTTP request. In our case just expanding the to_BusinessPartnerAddress field.
  - Proxy: The type of proxy that you are using to connect to the target system. In our case we are communicating with a cloud system, therefore we select Internet. If we would be communicating with an on-premise system we will need to set it to On-Premise.
  - Method: Action that the HTTP request must perform. In our case a GET request.
  - Authentication: The mock server has no authentication enabled hence why we select None. In a real world scenario you would set up a communication user in SAP S/4HANA and deploy the credentials to the secure store available in SAP Cloud Integration. 
- Header Details:
  - Request Headers: List of header that you want to send to the target system. We don't need to send any request headers to the Business Partners mock service but this parameter will be set in a future exercise where we will need to pass a header parameter.
  - Response Headers: List of headers coming from the target system's response. They will be available in the exchange after the request.


## Deploy

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 

![Deployment status](assets/deployment-starting-to-started.gif)

Once deployed, and the runtime status is `✅ Started`, you can click the `Navigate to Manage Integration Content link` and it will take you to the details of the deployed content. An HTTP endpoint URL, similar to the one below, will be displayed in the UI.

![Deployed content - HTTP endpoint URL](assets/deployed-content.png)

> ℹ️ In case you don't see the HTTP endpoint URL immediately in the deployed content page, see [troubleshooting](../../troubleshooting.md#there-is-no-http-endpoint-url-on-the-deployed-content-page).

## Monitoring

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 

## Sending a request to our integration flow

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 

> ⚠️ The [URL's hostname](https://developer.mozilla.org/en-US/docs/Web/API/URL/hostname) where our integration flow is deployed (https://my-instance.it-cpi018-rt.cfapps.eu10-003.hana.ondemand.com/http/my-endpoint) is very similar to the URL's hostname we access the SAP Cloud Integration UI (https://my-instance.it-cpi018.cfapps.eu10-003.hana.ondemand.com/itspaces/). Make sure to use the correct hostname when invoking the integration flow, if not an HTML page will be returned as a response when trying to send a request to the integration flow. Can you spot the difference in the URL hostnames?

I'm getting an HTTP 403 error message when posting a message from Postman to SAP Cloud Integration. What can I do?
It's a 403, not a 401... meaning that you are authenticating well to the service but the user you are using for communication doesn't have the right roles assign to it. Make sure that the user, like to be your.email@company.com, has the 

## Summary

Now that you are familiar with the basic functionality of SAP API Business Hub and the Business Partner API, we are ready to start interacting with the services from which our integration will be extracting data.

## Further reading

* [Defining the JSON-to-XML converter](https://help.sap.com/docs/CLOUD_INTEGRATION/987273656c2f47d2aca4e0bfce26c594/2f75a807d7574f099170de52dd8f91e2.html?locale=en-US&version=Cloud)
* [Request Reply external call](https://help.sap.com/docs/CLOUD_INTEGRATION/987273656c2f47d2aca4e0bfce26c594/dc39fdd4a44d4b9a9eabb56f49434250.html?locale=en-US&version=Cloud)
* [Externalise parameters of an Integration flow](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/45b2a0772db94bd9b0e57bc82d8d3797.html?locale=en-US)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. Can you think of a problem that we might face if we set the `employee_id` property as a header property instead of as an exchange property?
2. In the receiver HTTP adapter we hardcoded a URL. How can we make parametrise this field or other fields in our integration flow?
3. How can we configure our integration flow so that any errors raised during the execution can be returned to the sender?

* [^1]: [Getting Started with Integration Flow Development](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/e5724cd84b854719973afe0356ea128b.html?locale=en-US&q=%22integration%20flow%22)
