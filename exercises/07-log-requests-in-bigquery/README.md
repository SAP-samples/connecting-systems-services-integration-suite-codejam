# Exercise 07 - Log request in BigQuery

In our [integration scenario](../../README.md#integration-scenario), it is mentioned that we need to log the requests received by the integration flow. These requests will be logged in a table that exists in BigQuery. We will achieve this by using SAP Open Connectors to simplify the connection between SAP Cloud Integration and Google's BigQuery. 


![Log requests in BigQuery](assets/diagrams/bigquery_data_flow.png)
<p align = "center">
<i>Exercise 07 - Data flow</i>
</p>

At the end of this exercise, you'll have successfully configured an instance of a BigQuery in SAP Open Connectors and modified the integration flow so that it logs every request received.

## BigQuery

As part of the [prerequisites](../../prerequisites.md#bigquery) of this CodeJam, you should have created a Google Cloud Platform account if you didn't have one and also create a dataset and a table, which will be used to log the requests received by the integration flow.

Before we can configure the connectivity between SAP Open Connectors and BigQuery, we will need to create an OAuth client which we need to set up an instance in SAP Open Connectors.

### Create an OAuth 2.0 application in Google Cloud Platform


#### (Optional) ⚠️ If you've not defined an OAuth consent screen before ⚠️

👉 In Google Cloud Platform, select the project and go to `API & Services > OAuth consent screen` - https://console.cloud.google.com/apis/credentials/consent. Set the `User Type` to `Internal` and the app configuration similar to the one in the screenshot below.

![OAuth consent screen](assets/oauth-consent-screen.png)
<p align = "center">
<i>OAuth consent screen</i>
</p>


#### Create an OAuth 2.0 Client

👉 Navigate to the Google Cloud Platform console and create an OAuth 2.0 client. In Google Cloud Platform, select the project and go to `API & Services > Credentials`. Create a credential for OAuth Client ID and select `Web application` as the application type. Make sure to add https://auth.cloudelements.io/oauth as an Authorised redirect URI. Once the client is created, copy the Client ID and Client secret as we will need them to configure an instance of BigQuery in SAP Open Connectors.

![CodeJam - OAuth 2.0 Client](assets/codejam-oauth-clientid.png)
<p align = "center">
<i>CodeJam - OAuth 2.0 Client</i>
</p>


## SAP Open Connectors

From the SAP Open Connectors website... 

    SAP Open Connectors is built from the ground up to bring API integration and management together with a data-centric approach.

    Our platform – combined with our unique Connectors – is designed to unify the developer experience across all kinds of applications and services. Regardless of the application’s backend – REST, SOAP, Proprietary SDK, Database, etc – SAP Open Connectors creates a unified API layer and standards-based implementation across every environment.

We will use Open Connectors to enable the connection between our integration flow and the BigQuery service. Through it we will create the record that logs the request sent by the sender participant of the integration flow.

### Set up a BigQuery instance in Open Connectors

👉 Access the Open Connectors UI, from within the SAP Integration Suite, and create an instance of the BigQuery connector. Once created, copy the Authorization header details displayed in the API docs.



In Open Connectors, go to Connectors and search for BigQuery and select Authenticate. It will open the configuration screen to create a new instance. Enter the required information and complete the authorization flow to grant Open Connectors access to BigQuery.

### Create a schema



### Test the BigQuery credentials in the API docs

Now that the authentication is complete, visit the API docs of the connector instance just created (Instances > Your connector > API Docs). In the API docs, select any method and copy the value included as an Authorization header, e.g. `User QNBF4V=, Organization a0f234e, Element d3jbWv5/xxx/yyyyyyy/zzzzxqrk=`. We will use this value to configure the Open Connector credentials in the next step.

👉 Make sure you complete


## SAP Cloud Integration

# Deploy security material in SAP Cloud Integration

👉 Go to your SAP Cloud Integration instance and create/deploy the security material (Monitor > Manage Security > Security Material) for BigQuery. This will be used by the integration flow to communicate with BigQuery.

| Name        | Type                               | Fields                                                                 |
| ----------- | ---------------------------------- | ---------------------------------------------------------------------- |
| OC_BigQuery | Open Connectors | Enter the `User`, `Organization`, and `Element` details from Open Connectors |

## Summary

Now that you are familiar with the basic functionality of SAP API Business Hub and the Business Partner API, we are ready to start interacting with the services from which our integration will be extracting data.

## Further reading

* [Link 1](https://blogs.sap.com/)
* [Link 2](https://blogs.sap.com/)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. First question.
2. Second question.
