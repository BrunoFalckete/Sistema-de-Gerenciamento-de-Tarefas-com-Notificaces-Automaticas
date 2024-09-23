const API_URL = "http://localhost:5000/tasks";

export async function getTasks() {
  const response = await fetch(API_URL);
  return response.json();
}

export async function createTask(task) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(task),
  });
  return response.json();
}
