# Exercise 03 - Building our first integration flow

At the end of this exercise, you'll have successfully created a simple integration flow that communicates with the SAP S/4HANA mock server.

> **What is an integration flow [^1]?** 
> 
> An integration flow allows you to specify how SAP Cloud Integration is to process a message. The modeling environment, provided in SAP Cloud Integration, allows you to design the details of message processing (its senders and receivers as well as the individual processing steps) with a graphical user interface.

//TODO: Include diagram

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

👉 Navigate to the `Artifacts` tab in your integration package, Add an Integration Flow, specify a Name and ID for the integration flow and click on the newly created integration flow.

| Field  | Value                       |
| ------ | --------------------------- |
| *Name* | Request Employee Dependants |
| *ID*   | RequestEmployeeDependants   |

> If the `Add button` is greyed out it means you are not in Edit mode. Click the `Edit button` in the upper right hand corner.

![Add artifact to package](assets/add-artifact.png)

When accessing the newly created integration flow you'll notice a couple of things:
![New integration flow](assets/new-integration-flow.png)
- There are no connections between the Sender and our integration process or the integration processes and the receiver.
- The palette is greyed out (*highlighted in orange*) and we are unable to modify the integration flow. This is because our integration flow is not in edit mode. To switch to edit mode, click the `Edit button`.
- 



## Deploy

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 


## Monitoring

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 

## Sending a request to our integration flow

Justo donec enim diam vulputate ut pharetra. Pulvinar proin gravida hendrerit lectus a. Leo a diam sollicitudin tempor id eu. Enim eu turpis egestas pretium aenean pharetra magna. Et molestie ac feugiat sed lectus vestibulum mattis. A iaculis at erat pellentesque. 

> ⚠️ The [URL's hostname](https://developer.mozilla.org/en-US/docs/Web/API/URL/hostname) where our integration flow is deployed (https://my-instance.it-cpi018-rt.cfapps.eu10-003.hana.ondemand.com/http/my-endpoint) is very similar to the URL's hostname we access the SAP Cloud Integration UI (https://my-instance.it-cpi018.cfapps.eu10-003.hana.ondemand.com/itspaces/). Make sure to use the correct hostname when invoking the integration flow, if not an HTML page will be returned as a response when trying to send a request to the integration flow. Can you spot the difference in the URL hostnames?

## Summary

Now that you are familiar with the basic functionality of SAP API Business Hub and the Business Partner API, we are ready to start interacting with the services from which our integration will be extracting data.

## Further reading

* [Link 1](https://blogs.sap.com/)
* [Link 2](https://blogs.sap.com/)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. First question.
2. Second question.

* [^1]: [Getting Started with Integration Flow Development](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/e5724cd84b854719973afe0356ea128b.html?locale=en-US&q=%22integration%20flow%22)
