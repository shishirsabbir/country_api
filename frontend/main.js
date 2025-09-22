import { greeting } from "./utils/utils.js";

document.addEventListener("DOMContentLoaded", () => {
  const messageElement = document.createElement("h1");
  messageElement.textContent = greeting("FastAPI & Jinja2");
  document.body.appendChild(messageElement);
  console.log("App loaded and JS is working!");
});
