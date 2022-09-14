# Running locally - Prerequisites

So you are interested in running the services locally, exciting! Here are the prerequisites of how you can run the services used in this CodeJam locally. 

> Make sure to complete the prerequisites listed in [prerequisites.md](prerequisites.md) before proceeding with the requirements included here.

## Hardware

* Cloud Connector: [Hardware requirements](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e23f776e4d594fdbaeeb1196d47bbcc0.html?locale=en-US#hardware) to install Cloud Connector in your local machine:
    
    |                 | Minimum                                           | Recommended                                     |
    | --------------- | ------------------------------------------------- | ----------------------------------------------- |
    | CPU             | Single core 3 GHz, x86-64 architecture compatible | Dual core 2 GHz, x86-64 architecture compatible |
    | Memory (RAM)    | 2 GB                                              | 4 GB                                            |
    | Free disk space | 3 GB                                              | 20 GB                                           |


## Software

* Cloud Connector: The software requirements for Cloud Connector can be found [here](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e23f776e4d594fdbaeeb1196d47bbcc0.html?locale=en-US#software).
* Docker: We will use Docker to run the services. Proceed to [install Docker Desktop](https://docs.docker.com/desktop/install/mac-install/) if not installed on your local machine.


## Local Services

You can find detailed instructions on how to run the services locally on each repositories' overview page:
- SAP S/4HANA Cloud Business Partner mock server: https://hub.docker.com/r/ajmaradiaga/s4-mock-server 
- Business Partner Dependants mock service: https://hub.docker.com/r/ajmaradiaga/businesspartner-dependants-mock-server

> The repositories also contain instructions on deploying the containers to the SAP BTP, Kyma runtime environment.
