import React, { useState, useEffect } from "react";
import "./App.css";
import TaskList from "./components/TaskList";
import { getTasks, createTask } from "./services/taskService";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    async function fetchTasks() {
      const tasksFromServer = await getTasks();
      setTasks(tasksFromServer);
    }
    fetchTasks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (newTask.trim()) {
      const task = { name: newTask };
      const createdTask = await createTask(task);
      setTasks([...tasks, createdTask]);
      setNewTask("");
    }
  };

  return (
    <div className="App">
      <h1>Gerenciador de Tarefas</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Nova tarefa"
        />
        <button type="submit">Adicionar Tarefa</button>
      </form>

      <TaskList tasks={tasks} />
    </div>
  );
}

export default App;
