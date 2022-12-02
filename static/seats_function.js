
// Remove flash from screen
function removeDivFlash(){

    // Create variable for div of flash
    const div = document.getElementById("div_flash");

    // Create variable for button in flash
    const btn = document.getElementById("btn_flash")

    // Remove div
    div.remove();

    // Remove button
    btn.remove();
}