document.getElementById("btn").addEventListener("click", async () => {

    const file = document.getElementById("pdf").files[0];
    const output = document.getElementById("output");

    if (!file) {
        alert("Select PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    output.innerHTML = "Analyzing... ⏳";

    try {

        const res = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json(); 
        console.log(data);

        const analysis = data.analysis;
        if (analysis.status === "error") {
    output.innerHTML = `
        <div class="card">
            <h2 style="color:red;">❌ ${analysis.message}</h2>
        </div>
    `;
    return;
}
output.innerHTML = `
    <div class="card">

        <h2>📊 ATS Score: ${analysis.ats_score}/100</h2>

        <div style="width:100%;background:#ddd;border-radius:10px;height:20px;">
            <div style="
                width:${analysis.ats_score}%;
                background:#4CAF50;
                height:20px;
                border-radius:10px;">
            </div>
        </div>

        <h3>🧠 Skills Found</h3>
        <p>${analysis.skills.join(", ")}</p>

        <h3>⚠️ Missing Skills</h3>
        <p>${analysis.missing_skills.join(", ")}</p>

        <h3>💡 Suggestions</h3>
        <ul>
            ${analysis.suggestions.map(s => `<li>${s}</li>`).join("")}
        </ul>

        <h3>📄 Resume Analysis</h3>
        <pre style="white-space:pre-wrap;font-family:Arial;">
${analysis.analysis_raw}
        </pre>

    </div>
`;  

} catch (err) {
    output.innerHTML = "Error: " + err.message;
    console.error(err);
}
});