import axios from "axios";

// Base URL of your backend
const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// If you have authentication, you can set the token like this:
// API.defaults.headers.common["Authorization"] = "Bearer " + token;

export const getTasks = () => API.get("/tasks");
export const addTask = (task) => API.post("/tasks", task);
export const updateTask = (id, task) => API.put(`/tasks/${id}`, task);
export const deleteTask = (id) => API.delete(`/tasks/${id}`);
