# Troubleshooting

This page intends to capture any issues that you might face while going through the exercises that are part of the CodeJam. 

## Cloud Integration

- #### Why am I unable to edit the integration flow?
    This is because our integration flow is not in edit mode. To switch to edit mode, click the `Edit button` (*upper right corner*).

- #### An internal server error occurred: End of input at line 1 column 1 path $.
    No body was sent in the request. Remember that our integration flow expects a JSON payload. See [request payload sample](exercises/03-build-first-integration-flow/assets/request-payload-sample.json).

- #### There is no HTTP endpoint URL on the deployed content page.
    In case you don't see the HTTP endpoint URL immediately on the deployed content page, it takes a couple of seconds before it is reflected in the UI. Refresh the web page a couple of times and it will then be displayed.

- #### I'm getting an HTTP 403 error message when posting a message to SAP Cloud Integration. What can I do?
    It's a 403, not a 401... meaning that you are authenticating well to the service but the user you are using for communication doesn't have the right roles assigned to it. Make sure that the user has the ESBMessagingSend.send role in the BTP Cockpit. See the roles set up for the instance in the [prerequisites - Create SAP Cloud Integration runtime client credentials](prerequisites.md#create-sap-cloud-integration-runtime-client-credentials).

## Postman

TBA
