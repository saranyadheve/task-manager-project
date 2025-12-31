import { useEffect, useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "./AuthContext";

export default function Dashboard() {
  const { token, logout } = useContext(AuthContext);
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const headers = { Authorization: `Bearer ${token}` };

  const loadTasks = async () => {
    const res = await axios.get("http://127.0.0.1:8000/tasks", { headers });
    setTasks(res.data.tasks);
  };

  const addTask = async () => {
    await axios.post(
      "http://127.0.0.1:8000/tasks",
      { title },
      { headers }
    );
    setTitle("");
    loadTasks();
  };

  const deleteTask = async (index) => {
    await axios.delete(`http://127.0.0.1:8000/tasks/${index}`, { headers });
    loadTasks();
  };

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div className="box">
      <h2>Dashboard</h2>

      <input
        placeholder="New Task"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={addTask}>Add</button>

      <ul>
        {tasks.map((t, i) => (
          <li key={i}>
            {t.title}
            <button onClick={() => deleteTask(i)}>❌</button>
          </li>
        ))}
      </ul>

      <button onClick={logout}>Logout</button>
    </div>
  );
}
