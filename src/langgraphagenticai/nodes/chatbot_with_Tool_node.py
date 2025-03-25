from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm = model

    

    def process(self, state: State) -> dict:

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])
        """
        this process generates input state with tool integration
        
        state["messages"][-1] fetches the last message 
        
        state["messages"] is empty, the condition if state["messages"]
          evaluates to False, and an empty string ("") is assigned to
            user_input instead of raising an error"""
        
        # message from user anc content has the latest message
        """self.llm.invoke(...) calls a language model (LLM) to generate a response.
         The input is structured as a list of dictionaries."""
        
        """
        Processes the input state and generates a response with tool integration.
        """
        

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
 
        

        
    
    
    
    
    
