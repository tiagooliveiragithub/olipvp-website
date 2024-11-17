function copyToClipboard(element) {
  // Find the closest copy-message sibling
  const message = element.nextElementSibling;

  // Get the text to copy
  const textToCopy = element.textContent.trim();

  navigator.clipboard.writeText(textToCopy).then(() => {
    message.textContent = "Copied!";
    message.classList.add("show-notification");

    // Hide the notification after 1.5 seconds
    setTimeout(() => {
      message.classList.remove("show-notification");
    }, 1500);
  }).catch((err) => {
    console.error("Failed to copy text: ", err);
  });
}