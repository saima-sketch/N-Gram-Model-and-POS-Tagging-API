
const API_URL = "http://127.0.0.1:5000";

let latestResults = [];

async function performTagging() {
    const sentence = document.getElementById("sentence").value.trim();
    const status = document.getElementById("status");
    const button = document.getElementById("tagButton");
    const resultsSection = document.getElementById("resultsSection");

    if (!sentence) {
        status.textContent = "Please enter a sentence first.";
        resultsSection.hidden = true;
        return;
    }

    button.disabled = true;
    status.textContent = "Analyzing sentence...";
    resultsSection.hidden = true;

    try {
        const response = await fetch(`${API_URL}/pos-tag`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: sentence })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to process the sentence.");
        }

        latestResults = data.results;

        const tokensContainer = document.getElementById("tokens");
        tokensContainer.replaceChildren();

        data.tokens.forEach(word => {
            const token = document.createElement("span");
            token.className = "token";
            token.textContent = word;
            tokensContainer.appendChild(token);
        });

        const resultsBody = document.getElementById("resultsBody");
        resultsBody.replaceChildren();

        data.results.forEach(item => {
            const row = document.createElement("tr");

            [item.word, item.tag, item.description].forEach(value => {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            });

            resultsBody.appendChild(row);
        });

        resultsSection.hidden = false;
        status.textContent = "POS tagging completed successfully.";

    } catch (error) {
        status.textContent =
            `Error: ${error.message}. Make sure the Python backend is running.`;
    } finally {
        button.disabled = false;
    }
}

function downloadCSV() {
    if (!latestResults.length) {
        document.getElementById("status").textContent =
            "Perform POS tagging before downloading results.";
        return;
    }

    const rows = [
        ["Word", "POS Tag", "Description"],
        ...latestResults.map(item => [
            item.word,
            item.tag,
            item.description
        ])
    ];

    const csv = rows.map(row =>
        row.map(value =>
            `"${String(value).replace(/"/g, '""')}"`
        ).join(",")
    ).join("\r\n");

    const blob = new Blob(["\uFEFF" + csv], {
        type: "text/csv;charset=utf-8;"
    });

    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");

    link.href = url;
    link.download = "pos_tagging_results.csv";

    document.body.appendChild(link);
    link.click();
    link.remove();

    URL.revokeObjectURL(url);
}
