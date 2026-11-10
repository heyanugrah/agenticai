import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

# Load environment variables
load_dotenv(verbose=True)


# Define the state schema for your pipeline
class PipelineState(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str


# Initialize the Groq LLM
# Ensure GROQ_API_KEY is available in your .env file
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)


# STAGE 1: Editor Node
def editor_node(state: PipelineState) -> dict:
    """Clean grammar, remove typos and refine the tone."""

    print("\n--- [Stage 1] Executing Editor Node ---")

    prompt = (
        "You are an expert copyeditor. Clean up the following raw text. "
        "Fix any grammatical errors, spelling mistakes, and smooth out "
        "the transition flow while keeping the core message intact. "
        "Return only the edited text.\n\n"
        f"Text:\n{state['raw_input']}"
    )

    response = llm.invoke(prompt)

    # FIXED: Use edited_text, matching PipelineState
    return {
        "edited_text": response.content.strip()
    }


# STAGE 2: Scriptwriter Node
def scriptwriter_node(state: PipelineState) -> dict:
    """Formats the clean text into an engaging video script."""

    print("\n--- [Stage 2] Executing Scriptwriter Node ---")

    prompt = (
        "You are a charismatic YouTube content creator. "
        "Take this edited text and transform it into a highly "
        "engaging, punchy, conversational video script hook. "
        "Make it sound like a real person speaking passionately. "
        "Return only the script content.\n\n"
        f"Edited Text:\n{state['edited_text']}"
    )

    response = llm.invoke(prompt)

    return {
        "script_text": response.content.strip()
    }


# STAGE 3: Translator Node
def translator_node(state: PipelineState) -> dict:
    """Translates the script into natural flowing Hinglish."""

    print("\n--- [Stage 3] Executing Hinglish Translator Node ---")

    prompt = (
        "You are an expert content localizer for the Indian market. "
        "Take the following script and convert it into natural, "
        "flowing Hinglish. Do not simply translate it sentence by sentence "
        "or repeat information. Alternate comfortably between Hindi "
        "and English phrases just like an intellectual tech educator "
        "would speak naturally on a livestream. Keep the energy high! "
        "Return only the final Hinglish text.\n\n"
        f"Script:\n{state['script_text']}"
    )

    response = llm.invoke(prompt)

    return {
        "final_output": response.content.strip()
    }


# CREATE THE GRAPH
graph = StateGraph(PipelineState)


# ADD NODES
graph.add_node("editor", editor_node)
graph.add_node("scriptwriter", scriptwriter_node)
graph.add_node("translator", translator_node)


# ADD EDGES (Sequential workflow)
graph.add_edge(START, "editor")
graph.add_edge("editor", "scriptwriter")
graph.add_edge("scriptwriter", "translator")
graph.add_edge("translator", END)


# COMPILE THE GRAPH
app = graph.compile()


# EXECUTE THE GRAPH
result = app.invoke({
    "raw_input": (
        "AI agents are the future of tech. "
        "They can think, plan, and act on their own. "
        "LangGraph helps you build these agents "
        "with proper control and memory."
    )
})


# DISPLAY OUTPUT
print("\n========== FINAL RESULT ==========\n")
print(result["final_output"])
