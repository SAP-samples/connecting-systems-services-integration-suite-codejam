# Exercise 02 - Exploring the mock services

Before attempting to build an integration between the services, it is important to get familiar with them. The easiest way to achieve this is to use a REST client, e.g. Postman, to interact with the API exposed by the service. 

A couple of things that we need to keep in mind when interacting with the services:
- Is there any documentation that can guide us on the API, e.g. OpenAPI.
- What do we need to authenticate with the service?
- What are the API methods that we need to interact type of data, 
- Are there any API rate limits that we need to worry about?

> If you are following this exercise outside of a CodeJam event, you can follow the instructions included in [Optional Exercise 01 - Running and deploying the mock services](../optional-01-deploy-mock-services/README.md) to either run the services locally or deploy them to a [Kyma environment part of the SAP BTP](https://discovery-center.cloud.sap/serviceCatalog/kyma-runtime?region=all).

At the end of this exercise, you'll have an understanding of the data that we will be interacting with when building our first integration flow.

## Importing collections and environments of the mock services

A collection and a few environments are included in this repository to facilitate interacting with the APIs exposed by the services that we will be using in our integration. The collection and environments for the S/4HANA mock server and the Business Partner Dependants mock service can be found in the assets folder, under the [s4-mock-server](assets/s4-mock-server/) and [bp-dependants-mock-service](assets/bp-dependants-mock-service/) folders respectively.

> - [Postman Collections](https://www.postman.com/collection/): Postman Collections are Executable API Descriptions. Postman's collection folders make it easy to keep your API requests and elements organized. 
> - [Postman enviroment](https://learning.postman.com/docs/sending-requests/managing-environments/): A Postman environment is a set of variables you can use in your Postman requests. You can use environments to group related sets of values together and manage access to shared Postman data if you are working as part of a team.

👉 Import the collection and the environments provided to your Postman client.

Below, the files that you need to import to Postman:
```
Collection:
- ../assets/connecting-services-integration-suite-codejam.postman_collection.json

Environments:
- ../assets/bp-dependants-mock-service/BP-Dependants-Americas.postman_environment.json
- ../assets/bp-dependants-mock-service/BP-Dependants-EU.postman_environment.json
- ../assets/s4-bp-mock-server/S4-BP-Mock-Server.postman_environment.json
```

![Import objects to Postman](assets/import-objects-to-Postman.gif)



## SAP S/4HANA Cloud - Business Partner mock service

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat..

👉 Make sure you complete


## Custom Service - Business Partner Dependants mock service

Lets start by validating that the API is up and running 

👉 Send a Ping request to the service


## Summary

Now that you are familiar with the APIs and the data included in their responses, we are ready to start building our first integration flow.

## Further reading

* [Link 1](https://blogs.sap.com/)
* [Link 2](https://blogs.sap.com/)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. First question.
2. Second question.

## Next

Continue to 👉 [Exercise 03 - Building the first integration flow](../03-build-first-integration-flow/README.md)