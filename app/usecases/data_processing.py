from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

AVERAGE_Z_IN_DATA = 14352

def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    z_position = agent_data.accelerometer.z - AVERAGE_Z_IN_DATA

    if -100 <= z_position <= 100:
        road_state = "perfect"
    elif -800 <= z_position <= 800:
        road_state = "good"
    elif -2000 <= z_position <= 2000:
        road_state = "norm"
    elif -10000 <= z_position <= 10000:
        road_state = "bad"
    else:
        road_state = "very bad"

    agent_data.user_id = 0

    return ProcessedAgentData(road_state=road_state, agent_data=agent_data)
