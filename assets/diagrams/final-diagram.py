# tech-byte-diagram.py
from diagrams import Cluster, Diagram, Edge, Node
from diagrams.onprem.compute import Server
from diagrams.generic.compute import Rack
from diagrams.generic.place import Datacenter
from diagrams.custom import Custom
from diagrams.sap.other import Placeholder_Circle
from diagrams.sap.integration import ProcessIntegration_Circle, OpenConnectors_Circle, APIManagement_Circle
from diagrams.sap.runtimes import KymaRuntime_Circle
from diagrams.gcp.analytics import BigQuery
from diagrams.sap.erp import SAPS4HANACloud

# SAP BTP Solution Diagrams and Icons guidelines colors
L0_BLUE_COLOUR = "#316CCA"
L1_BLUE_COLOUR = "#074D92"
L2_GREEN_COLOUR = "#0F828F"
FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

GLOBALACCOUNT_GRAPH_ATTR = {"bgcolor": "white",
                            "pencolor": L0_BLUE_COLOUR, "penwidth":"3.0", "fontname": "72 Bold"}
SUBACCOUNT_GRAPH_ATTR = {"bgcolor": "white",
                         "pencolor": L1_BLUE_COLOUR, "penwidth":"2.5", "fontname": "72 Bold Italic"}
PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR = {
    "bgcolor": "white", "pencolor": L2_GREEN_COLOUR, "penwidth":"2.0", "style": "dashed", "fontname": "72 Italic"}

NODE_LABEL = {"fontname": "72 Regular"}
EDGE_LABEL = {"color": FIX_GREY_COLOUR, "fontname": "72 Italic"}

with Diagram("", show=False, filename="final_data_flow", graph_attr={"splines": "true"}):
    rest_client = Custom("REST Client", "../postman-logo.png")
    benefits_platform = Server("Benefits Platform", **NODE_LABEL)
    sap_server = SAPS4HANACloud(**{"height": "2.5", "width": "2.5"})
    big_query = BigQuery("Logs")

    with Cluster("SAP Business Technology Platform - CodeJam account", graph_attr=GLOBALACCOUNT_GRAPH_ATTR):
        with Cluster("Americas Subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            americas_service = KymaRuntime_Circle("BP Dependants\nService", **NODE_LABEL)

        with Cluster("European Subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            european_service = KymaRuntime_Circle("BP Dependants\nService", **NODE_LABEL)
            
    with Cluster("SAP Business Technology Platform - Participant account", graph_attr=GLOBALACCOUNT_GRAPH_ATTR):
        with Cluster("Your Subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            with Cluster("SAP Integration Suite", graph_attr=PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR):
                cloud_integration = ProcessIntegration_Circle("Cloud Integration", **NODE_LABEL)
                api_management = APIManagement_Circle("API Management", **NODE_LABEL)
                open_connectors = OpenConnectors_Circle("Open Connectors", **NODE_LABEL)
                
                cloud_integration >> Edge(label="Business Partners", **EDGE_LABEL) >> sap_server

                open_connectors >> Edge(label="Log request", **EDGE_LABEL) >> big_query

                cloud_integration >> americas_service

                cloud_integration >> Edge(label="Dependants", **EDGE_LABEL) >> european_service


                benefits_platform >> Edge(label="Send request", orientation="135", **EDGE_LABEL) >> api_management
                rest_client >> Edge(label="Send request", **EDGE_LABEL) >> api_management
                api_management - cloud_integration - open_connectors

                
