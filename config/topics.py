# config/topics.py
# MQTT Topic definitions for the SUPCON AdventureX Factory Simulation

# Device status topics (published by factory devices)
# STATION_STATUS_TOPIC = "AgenticFactoria/{line}/station/{device_id}/status"
# AGV_STATUS_TOPIC = "AgenticFactoria/{line}/resource/{device_id}/status"
# QUALITY_CHECKER_STATUS_TOPIC = "AgenticFactoria/{line}/quality/{device_id}/status"
NEW_FACTORY_STATUS_TOPIC = "AgenticFactoria/{line}/{device_type}/{device_id}/status"
FACTORY_STATUS_TOPIC = "AgenticFactoria/{line}/status"

# Buffer full alert topics (published by fault system)
BUFFER_FULL_ALERT_TOPIC = "AgenticFactoria/line1/alerts/buffer_full"
AGV_BATTERY_LOW_ALERT_TOPIC = "AgenticFactoria/line1/alerts/agv_battery_low"

# Order and KPI topics
NEW_ORDER_TOPIC = "AgenticFactoria/line1/orders/status"
KPI_UPDATE_TOPIC = "AgenticFactoria/line1/kpi/status"
RESULT_TOPIC = "AgenticFactoria/line1/result/status"
# Agent command topics (published by AI agents)
AGENT_COMMANDS_TOPIC = "AgenticFactoria/line1/agent/commands"
# Agent response topics (subscribed by AI agents)
AGENT_RESPONSES_TOPIC = "AgenticFactoria/line1/agent/responses"

# Natural language logs for visualization
NL_LOGS_TOPIC = "AgenticFactoria/{line}/agent/nl_logs"

# Topic patterns for subscription
ALL_STATION_STATUS = "AgenticFactoria/{line}/station/+/status"
ALL_AGV_STATUS = "AgenticFactoria/{line}/resource/+/status"
ALL_FACTORY_TOPICS = "AgenticFactoria/{line}/+"

# Legacy topic definitions (keeping for backward compatibility)
STATION_STATUS_TOPIC_PREFIX = "AgenticFactoria/line1/station"
CONVEYOR_STATUS_TOPIC_PREFIX = "AgenticFactoria/line1/conveyor"
AGV_STATUS_TOPIC_PREFIX = "AgenticFactoria/line1/agv"
WAREHOUSE_STATUS_TOPIC_PREFIX = "AgenticFactoria/line1/warehouse"
DEVICE_ALERT_TOPIC = "AgenticFactoria/line1/alerts"


def get_station_status_topic(station_id: str) -> str:
    """Returns the status topic for a specific station."""
    return f"{STATION_STATUS_TOPIC_PREFIX}/{station_id}/status"


def get_conveyor_status_topic(conveyor_id: str) -> str:
    """Returns the status topic for a specific conveyor."""
    return f"{CONVEYOR_STATUS_TOPIC_PREFIX}/{conveyor_id}/status"


def get_agv_status_topic(agv_id: str) -> str:
    """Returns the status topic for a specific AGV."""
    return f"{AGV_STATUS_TOPIC_PREFIX}/{agv_id}/status"


def get_warehouse_status_topic(warehouse_id: str) -> str:
    """Returns the status topic for a specific warehouse."""
    return f"{WAREHOUSE_STATUS_TOPIC_PREFIX}/{warehouse_id}/status"
