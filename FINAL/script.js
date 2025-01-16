// Function to adjust the page scale based on screen width
function adjustScale() {
    const width = window.innerWidth; // Get the current window width
    let scale = 1; // Default scale factor

    // Determine the scale factor based on the screen width
    if (width <= 600) {
        scale = 0.5;
    } else if (width > 600 && width <= 700) {
        scale = 0.75;
    } else if (width > 700 && width <= 767) {
        scale = 0.8;
    } else if (width >= 992 && width <= 1600) {
        scale = 0.9;
    } else {
        scale = 1; // No scaling for other widths
    }

    // Apply the scaling transformation to the body
    document.body.style.transform = `scale(${scale})`;
    document.body.style.transformOrigin = 'top left'; // Ensure scaling starts from the top-left corner
}

// Event listeners for window resizing and initial page load
window.addEventListener('resize', adjustScale);
window.addEventListener('DOMContentLoaded', adjustScale);
