import React from "react";

function TaskList({ tasks }) {
  return (
    <div>
      <h2>Suas Tarefas</h2>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
