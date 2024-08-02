import streamlit as st
import functions

todos = functions.get_todo()
def add_todo():
    todo = st.session_state['input_todo'] + "\n"
    todos.append(todo)
    functions.write_todo(todos)
    st.session_state['input_todo'] = ""


st.title("My To-Do App")
st.subheader("App to maintain todos")
st.write("click on checkbox to delete a todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
        # st.experimental_rerun()
st.text_input(label="", placeholder="Add a ToDo",key='input_todo',on_change=add_todo)

st.session_state



