// Create a new HTML element for the main window
const root = document.createElement('div');
root.style.width = '1080px'; // sets width for main window
root.style.height = '720px'; // sets height for main window
root.style.border = '1px solid black'; // adds a border to the main window
root.style.display = 'flex'; // enables flexbox layout
root.style.alignItems = 'center'; // centers items vertically
root.style.justifyContent = 'center'; // centers items horizontally
document.body.appendChild(root); // appends the main window to the body

// Create a label for the main window
const label = document.createElement('h1'); // creates an h1 element for the label
label.textContent = 'MY FIRST WINDOW'; // sets the text for the label
root.appendChild(label); // appends the label to the main window