# Connecting Systems and Services Using SAP Integration Suite

[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/connecting-systems-services-integration-suite-codejam)](https://api.reuse.software/info/github.com/SAP-samples/connecting-systems-services-integration-suite-codejam)

---
## *SAP CodeJam events scheduled*

- 2022-09-29: 🇪🇸 SAP CodeJam BTP: Connecting systems and services using SAP Integration Suite (Madrid, Spain) - [✅](https://groups.community.sap.com/t5/sap-codejam/sap-codejam-btp-connecting-systems-and-services-using-sap/ec-p/9782#M21).
- 2022-10-28: 🇪🇸 SAP CodeJam BTP: Connecting systems and services using SAP Integration Suite (Barcelona, Spain) - [✅](https://groups.community.sap.com/t5/sap-codejam/sap-codejam-btp-connecting-systems-and-services-using-sap/ec-p/9961#M32).

---

Welcome to the Connecting Systems and Services Using SAP Integration Suite CodeJam repository. In this SAP CodeJam, we will look at different services part of the SAP Integration Suite and how we can use them to connect our systems and services. By the end of the CodeJam, we will achieve an integration scenario like the one below in the diagram.

![Final data flow](assets/diagrams/final_data_flow.png)

## Integration Scenario

Let's imagine we work for a company, ITeLO. ITeLO uses an external platform to manage its Employee Benefits, through which its employees can select their benefits, e.g. discount gym membership, private health insurance, and dental. In addition, ITeLO is interested in expanding its adoption of the benefits platform to allow employees to include their dependants, e.g. spouse, child or other family members, as beneficiaries of the different offerings available on the platform. 

Currently, the benefits platform only has basic employee information, e.g. employee ID, personal email address, full name, and additional data will need to be shared to include dependants as beneficiaries. These employee dependant data exist within ITeLO's systems, and the benefits platform will need to communicate with these systems to retrieve employee dependant data. The employee dependant data is distributed across different geographies, Americas and the European Union (EU). The Americas server stores data for employees in the American continent, whilst the EU instance stores data for employees in the EU. 

We are in charge of building the integration scenario to allow the benefits platform access to the employee dependants' data.
  
The benefits platform will not store employee dependant data and will send our integration service a message whenever it needs an employee dependants' data. We will need to validate the employee ID sent in the message against our global SAP S/4HANA Cloud system before retrieving the employee dependant data from the servers hosting the data. Also, our integration service will need to log the requests received.

## Prerequisites

The prerequisites to follow the exercises in this repository, including hardware and software, are detailed in the [prerequisites](prerequisites.md) file.

## Material organization

The material consists of a series of exercises. These exercises build on each other and should be completed in the given order. For example, we start by creating a simple integration flow, and we will extend it in the subsequent exercises.

The repository includes some [slides](slides.md), which will be used when running an SAP CodeJam event. The slides were built using [Marp](https://github.com/marp-team/marp/) and an HTML export is included [here](slides.html). You can also [preview the slides here](https://htmlpreview.github.io/?https://github.com/SAP-samples/connecting-systems-services-integration-suite-codejam/blob/main/slides.html).

## Exercises

During the CodeJam you will complete each exercise one at a time. At the end of each exercise, questions are included to help you think about the content just covered and are to be discussed with the entire CodeJam class, led by the instructor, when everyone has finished that exercise.

If you finish an exercise early, please resist the temptation to continue with the next one. Instead, explore what you've just done and see if you can learn more about the subject covered. That way, we all stay on track together and can benefit from some reflection via the questions (and answers).

See below for an overview of the exercises part of this CodeJam.

* Please ensure that you have completed all the [prerequisites](prerequisites.md).
* Exercises:
  * [Exercise 01 - Getting familiar with the SAP API Business Hub](./exercises/01-getting-familiar-api-business-hub/README.md#exercise-01---getting-familiar-with-the-sap-api-business-hub)
  * [Exercise 02 - Exploring the mock services](./exercises/02-exploring-the-mock-services/README.md#exercise-02---exploring-the-mock-services)
  * [Exercise 03 - Build our first integration flow (Cloud Integration)](./exercises/03-build-first-integration-flow/README.md#exercise-03---building-our-first-integration-flow)
  * [Exercise 04 - Send messages and monitor our integration flow](./exercises/04-send-messages-and-monitor/README.md#exercise-04---sending-messages-and-monitoring-our-integration-flow)
  * [Exercise 05 - Retrieve Business Partner dependant's information](./exercises/05-retrieve-bp-dependants/README.md#exercise-05---retrieve-business-partner-dependants-information)
  * [Exercise 06 - Add the America's instance of the Business Partner Dependants service](./exercises/06-add-americas-bp-dependants/README.md#exercise-06---add-the-americas-instance-of-the-business-partner-dependants-service)
  * [Exercise 07 - Log service call in Google BigQuery (Open Connectors)](./exercises/07-log-requests-in-bigquery/README.md#exercise-07---log-request-in-bigquery)
  * [Exercise 08 - Expose integration flow via API Management](./exercises/08-expose-integration-flow-api-management/README.md#exercise-08---expose-integration-flow-via-api-management)
  * [(Optional) Exercise 01 - Running locally services used in CodeJam](./exercises/optional-01-running-locally/README.md#optional-exercise-01---running-locally-services-used-in-codejam)

### Troubleshooting

While going through the exercises, you might encounter common problems not explicitly related to them. Check out the [troubleshooting.md](troubleshooting.md) page, which includes a list of these common problems and their potential solutions.

## Known Issues

None

## Feedback

If you can spare a couple of minutes at the end of the session, please help us improve for next time by giving me some feedback.

Simply use this [Give Feedback](https://github.com/SAP-samples/connecting-systems-services-integration-suite-codejam/issues/new?assignees=&labels=feedback&template=session-feedback-template.md&title=Feedback) link to create a special "feedback" issue, and follow the instructions there.

Gracias/Thank you/Obrigado/Merçi/Danke!

## How to obtain support
Support for the content in this repository is available during CodeJam events, for which this content has been designed.

Alternatively, if you are completing this CodeJam on your own, outside of an event, you can [create an issue](https://github.com/SAP-samples/connecting-systems-services-integration-suite-codejam/issues/new) in this repository if you find a bug or have questions about it.
 
For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## Contributing
Please send a pull request if you wish to contribute code or offer fixes or improvements. Due to legal reasons, contributors will need to accept a DCO when they create the first pull request for this project. This happens in an automated fashion during the submission process. SAP uses [the standard DCO text of the Linux Foundation](https://developercertificate.org/).

## License
Copyright (c) 2022 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
