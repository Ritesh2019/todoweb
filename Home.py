import streamlit as st
from functions import read_todo,write_todo
todos = read_todo()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todo(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("Todos Application")
st.write("This is a todo app to maintain your daily todos")
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todo",placeholder="Enter a new todo",on_change=add_todo,key="new_todo")


