import warnings
import logging
warnings.filterwarnings("ignore")
logging.disable(logging.CRITICAL)

import gradio as gr
from rag import ask
# ... rest of your code stays same

import gradio as gr
from rag import ask


def chat(user_message, history):
    if not user_message.strip():
        return history, history, ""

    response = ask(user_message)
    history = history or []
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": response})
    return history, history, ""


def quick_ask(question, history):
    return chat(question, history)


with gr.Blocks(title="University Chatbot") as demo:

    gr.Markdown(
        "<div style='text-align:center; padding:10px;'>"
        "<h1>🎓 University RAG Chatbot</h1>"
        "<p>Ask anything about admissions, fees, courses and placements</p>"
        "</div>"
    )

    with gr.Row():

        with gr.Column(scale=1):
            gr.Markdown("### 📌 Quick Questions")
            q1 = gr.Button("Admission Process")
            q2 = gr.Button("All Schools & Departments")
            q3 = gr.Button("Placement Package")
            q4 = gr.Button("Available Courses")
            q5 = gr.Button("Hostel Facility")
            gr.Markdown("---")
            gr.Markdown("### ℹ️ About")
            gr.Markdown(
                "- 📄 Source: College Dataset PDF\n"
                "- 🧠 Model: Mistral 7B\n"
                "- 🔍 Search: ChromaDB\n"
                "- 🤗 Embeddings: MiniLM-L6"
            )

        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                height=500,
                show_label=False,
                avatar_images=("👤", "🎓")
            )
            with gr.Row():
                user_input = gr.Textbox(
                    placeholder="Type your question here...",
                    label="",
                    scale=5
                )
                send_btn = gr.Button("Send 🚀", variant="primary", scale=1)
            clear_btn = gr.Button("🗑️ Clear", variant="secondary")
            state = gr.State([])

    gr.Markdown(
        "<div style='text-align:center; color:gray; font-size:12px; padding:10px;'>"
        "Built with LangChain • ChromaDB • Mistral 7B • Gradio"
        "</div>"
    )

    send_btn.click(fn=chat, inputs=[user_input, state], outputs=[chatbot, state, user_input])
    user_input.submit(fn=chat, inputs=[user_input, state], outputs=[chatbot, state, user_input])
    clear_btn.click(fn=lambda: ([], [], ""), outputs=[chatbot, state, user_input])

    q1.click(fn=lambda h: quick_ask("What is the admission process?", h), inputs=[state], outputs=[chatbot, state, user_input])
    q2.click(fn=lambda h: quick_ask("What are all the schools and departments in the university?", h), inputs=[state], outputs=[chatbot, state, user_input])
    q3.click(fn=lambda h: quick_ask("What is the placement package?", h), inputs=[state], outputs=[chatbot, state, user_input])
    q4.click(fn=lambda h: quick_ask("What courses are available?", h), inputs=[state], outputs=[chatbot, state, user_input])
    q5.click(fn=lambda h: quick_ask("Is hostel facility available?", h), inputs=[state], outputs=[chatbot, state, user_input])


if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())