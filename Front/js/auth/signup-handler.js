function validateUsername() {
  const usernameInput = document.getElementById("usernameSignupForm");
  const usernameHelp = document.getElementById("usernameHelp");
  const username = usernameInput.value;

  if (username.length < 4) {
    usernameHelp.innerText = "Username must be at least 4 characters";
    usernameInput.classList.add("is-invalid");
    usernameInput.classList.remove("is-valid");
    return false;
  } else {
    usernameHelp.innerText = "";
    usernameInput.classList.remove("is-invalid");
    usernameInput.classList.add("is-valid");
    return true;
  }
}

// Validation function for fullname
function validateFullname() {
  const fullnameInput = document.getElementById("fullname");
  const fullnameHelp = document.getElementById("fullnameHelp");
  const fullname = fullnameInput.value;

  if (fullname.length < 4) {
    fullnameHelp.innerText = "Fullname must be at least 4 characters";
    fullnameInput.classList.add("is-invalid");
    fullnameInput.classList.remove("is-valid");
    return false;
  } else {
    fullnameHelp.innerText = "";
    fullnameInput.classList.remove("is-invalid");
    fullnameInput.classList.add("is-valid");
    return true;
  }
}

// Validation function for email
function validateEmail() {
  const emailInput = document.getElementById("email");
  const emailHelp = document.getElementById("emailHelp");
  const email = emailInput.value;

  // You can add more sophisticated email validation logic here
  if (!email.includes("@")) {
    emailHelp.innerText = "Invalid email address";
    emailInput.classList.add("is-invalid");
    emailInput.classList.remove("is-valid");
    return false;
  } else {
    emailHelp.innerText = "";
    emailInput.classList.remove("is-invalid");
    emailInput.classList.add("is-valid");
    return true;
  }
}

// Event listeners for input validation
document
  .getElementById("usernameSignupForm")
  .addEventListener("input", validateUsername);
document.getElementById("fullname").addEventListener("input", validateFullname);
document.getElementById("email").addEventListener("input", validateEmail);

const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");
const passwordHelp = document.getElementById("passwordHelp");
const confirmPasswordHelp = document.getElementById("confirmPasswordHelp");

function validatePassword() {
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  if (!checkPasswordStrength(password))
    passwordHelp.innerText = "Expected 8 or more characters";

  if (password !== confirmPassword) {
    confirmPasswordHelp.innerText = "Passwords do not match";
    return false;
  } else {
    confirmPasswordHelp.innerText = "";
    return true;
  }
}

function checkPasswordStrength(password) {
  if (password.length >= 8) {
    return false;
  } else {
    return true;
  }
}

// Validation function for confirm password
function validateConfirmPassword() {
  const confirmPasswordInput = document.getElementById("confirmPassword");
  const confirmPasswordHelp = document.getElementById("confirmPasswordHelp");
  const confirmPassword = confirmPasswordInput.value;
  const password = document.getElementById("password").value;

  if (confirmPassword !== password) {
    if (checkPasswordStrength(password))
      passwordHelp.innerText = "";
    confirmPasswordHelp.innerText = "Passwords do not match";
    confirmPasswordInput.classList.add("is-invalid");
    confirmPasswordInput.classList.remove("is-valid");
    passwordInput.classList.add("is-invalid");
    passwordInput.classList.remove("is-valid");
    return false;
  } else {
    confirmPasswordHelp.innerText = "";
    confirmPasswordInput.classList.remove("is-invalid");
    confirmPasswordInput.classList.add("is-valid");
    passwordInput.classList.remove("is-invalid");
    passwordInput.classList.add("is-valid");
    return true;
  }
}

// Event listeners for input validation
document.getElementById("password").addEventListener("input", validatePassword);
document
  .getElementById("confirmPassword")
  .addEventListener("input", validateConfirmPassword);

const tryFormPost = async () => {
  const username = document.getElementById("usernameSignupForm").value;
  const fullname = document.getElementById("fullname").value;
  const password = document.getElementById("password").value;

  token = await getCsrfToken();

  fetch("http://localhost:8000/api/user/signup/", {
    method: "POST",
    mode: "cors",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
    body: JSON.stringify({
      username: username,
      fullname: fullname,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "ok") {
        sessionStorage.setItem("username", username);
        sessionStorage.setItem("jwt", data.token);
        window.location.href = "/home";
      } else {
        console.error("Error:", data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const form = document.getElementById("signupForm");
form.addEventListener(
  "submit",
  function (event) {
    event.preventDefault();
    if (
      !validateUsername() ||
      !validateFullname() ||
      !validateEmail() ||
      !validatePassword() ||
      !validateConfirmPassword()
    ) {
      return;
    }
    tryFormPost();
  },
  false
);
