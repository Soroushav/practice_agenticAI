from dataclasses import dataclass

import os
import glob
import random

from autogen_core import AgentId

@dataclass
class Message:
    content: str

def find_recipient() -> AgentId:
    try:
        agents = glob.glob("agent*.py")
        agent_names = [os.path.splitext(agent)[0] for agent in agents]
        agent_names.remove("agent")
        agent_name = random.choice(agent_names)
        print(f"Selecting agent for refinement: {agent_name}")
        return AgentId(agent_name, "default")
    except Exception as e:
        print(f"Exception finding recipient: {e}")
        return AgentId("agent1", "default")
