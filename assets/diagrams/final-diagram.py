# tech-byte-diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.custom import Custom
from diagrams.sap.integration_suite import CloudIntegration, APIManagement
from diagrams.sap.foundational import SAPBTPKymaRuntime
from diagrams.saas.chat import Slack
from diagrams.sap.brands import SAPS4HANACloud

# SAP BTP Solution Diagrams and Icons guidelines colours

# SAP Areas
L0_BORDER_COLOUR = "#0070F2"
L0_FILLED_COLOUR = "#EBF8FF"
L1_BORDER_COLOUR = "#0070F2"
L1_FILLED_COLOUR = "#FFFFFF"
L2_GREEN_COLOUR = "#0F828F"
SUCCESS_GREEN_COLOUR = "#188918"
SUCCESS_FILLED_COLOUR = "#F5FAE5"

TEAL_BORDER_COLOUR = "#07838F"
TEAL_FILLED_COLOUR = "#DAFDF5"

INDIGO_BORDER_COLOUR = "#5D36FF"
INDIGO_FILLED_COLOUR = "#F1ECFF"

PINK_BORDER_COLOUR = "#5D36FF"
PINK_FILLED_COLOUR = "#FFF0FA"

# Non-SAP Areas
L0_NON_SAP_BORDER_COLOUR = "#475E75"
L0_NON_SAP_FILLED_COLOUR = "#F5F6F7"
L1_NON_SAP_BORDER_COLOUR = "#595959"
L1_NON_SAP_FILLED_COLOUR = "#FFFFFF"

FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

PRODUCER_COLOUR = "#07838F"
CONSUMER_COLOUR = "#5D36FF"

GLOBALACCOUNT_GRAPH_ATTR = {"bgcolor": L0_FILLED_COLOUR,
                            "pencolor": L0_BORDER_COLOUR, "penwidth":"3.0", "fontname": "72 Bold"}
SUBACCOUNT_GRAPH_ATTR = {"bgcolor": L1_FILLED_COLOUR,
                         "pencolor": L1_BORDER_COLOUR, "penwidth":"2.5", "fontname": "72 Bold"}
PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR = {
    "bgcolor": TEAL_FILLED_COLOUR, "pencolor": TEAL_BORDER_COLOUR, "penwidth":"2.0", "fontname": "72 Regular"}

NODE_LABEL = {"fontname": "72 Regular"}
EDGE_LABEL = {"color": FIX_GREY_COLOUR, "fontname": "72 Italic"}

with Diagram("", show=False, filename="final_data_flow", graph_attr={"splines": "true"}):
    rest_client = Custom("REST Client", "../bruno-logo.png")
    benefits_platform = Server("Benefits Platform", **NODE_LABEL)
    sap_server = SAPS4HANACloud(**{"height": "2.5", "width": "2.5"})
    slack = Slack("Logs")

    with Cluster("SAP Business Technology Platform - CodeJam account", graph_attr=GLOBALACCOUNT_GRAPH_ATTR):
        with Cluster("Americas subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            americas_service = SAPBTPKymaRuntime("BP Dependants\nService", **NODE_LABEL)

        with Cluster("European subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            european_service = SAPBTPKymaRuntime("BP Dependants\nService", **NODE_LABEL)
            
    with Cluster("SAP Business Technology Platform - Participant account", graph_attr=GLOBALACCOUNT_GRAPH_ATTR):
        with Cluster("Your subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            with Cluster("SAP Integration Suite", graph_attr=PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR):
                cloud_integration = CloudIntegration("Cloud Integration", **NODE_LABEL)
                api_management = APIManagement("API Management", **NODE_LABEL)
                
                cloud_integration >> Edge(label="Business Partners", **EDGE_LABEL) >> sap_server

                cloud_integration >> Edge(label="Log request", **EDGE_LABEL) >> slack

                cloud_integration >> americas_service

                cloud_integration >> Edge(label="Dependants", **EDGE_LABEL) >> european_service


                benefits_platform >> Edge(label="Send request", orientation="135", **EDGE_LABEL) >> api_management
                rest_client >> Edge(label="Send request", **EDGE_LABEL) >> api_management
                api_management - cloud_integration
