const API_URL = "http://localhost:8000";

document.getElementById("saveBtn").addEventListener("click", saveMessage);
document.getElementById("loadBtn").addEventListener("click", loadMessages);

async function saveMessage() {
  const input = document.getElementById("msgInput");

  await fetch(`${API_URL}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      content: input.value,
    }),
  });

  input.value = "";
}

async function loadMessages() {
  const box = document.getElementById("messagesBox");
  box.innerHTML = "Loading...";

  const res = await fetch(`${API_URL}/messages`);
  const data = await res.json();

  box.innerHTML = data
    .map((m) => `<div class="msg">#${m.id}: ${m.content}</div>`)
    .join("");
}
