// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
  const themeToggleButton = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const currentTheme = localStorage.getItem('theme') || 'light';

  // Define paths to your icons
  const moonIconPath = "/static/icons/moon.png";
  const sunIconPath = "/static/icons/sun.png";

  // Set the theme on page load
  if (currentTheme === 'dark') {
    document.body.classList.add('dark');
    themeIcon.src = sunIconPath;
    themeIcon.alt = "Day Theme";
  } else {
    themeIcon.src = moonIconPath;
    themeIcon.alt = "Night Theme";
  }

  // Toggle theme on button click
  themeToggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark');

    // Update the icon based on the theme
    if (document.body.classList.contains('dark')) {
      themeIcon.src = sunIconPath;
      themeIcon.alt = "Day Theme";
    } else {
      themeIcon.src = moonIconPath;
      themeIcon.alt = "Night Theme";
    }

    // Store the theme in localStorage
    const theme = document.body.classList.contains('dark') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
  });
});