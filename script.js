function findMatches() {
    const text = document.getElementById("testString").value;
    const regexPattern = document.getElementById("regexInput").value;
    const output = document.getElementById("output");

    output.innerHTML = "";

    try {
        const regex = new RegExp(regexPattern, "g");
        const matches = text.match(regex);

        if (matches) {
            matches.forEach((match, index) => {
                output.innerHTML += `<p>Match ${index + 1}: ${match}</p>`;
            });
        } else {
            output.innerHTML = "<p>No matches found.</p>";
        }
    } catch (error) {
        output.innerHTML = "<p style='color:red;'>Invalid Regular Expression</p>";
        console.error(error);
    }
}
