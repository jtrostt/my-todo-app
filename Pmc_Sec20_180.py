print("Section 20 - 180")
import sys
print(sys.version)
import streamlit as st
import Pmc_Functions_Sec19

todos = Pmc_Functions_Sec19.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Pmc_Functions_Sec19.write_todos(todos)


st.title("NEIL RULES THE UNIVERSE!")
st.subheader("And he's damn good at it")
st.write("All Hail the Mighty NEIL!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Pmc_Functions_Sec19.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#print("Refreshing...")

#st.session_state
