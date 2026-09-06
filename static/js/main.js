const dropzone = document.getElementById("dropzone");
const dropzoneText = document.getElementById("dropzone-text");
const fileInput = document.getElementById("file-input");
const jobDescriptionEl = document.getElementById("job-description");
const analyzeBtn = document.getElementById("analyze-btn");
const statusLine = document.getElementById("status-line");

const emptyState = document.getElementById("empty-state");
const resultsContent = document.getElementById("results-content");
const detailGrid = document.getElementById("detail-grid");
const skillsList = document.getElementById("skills-list");
const educationList = document.getElementById("education-list");
const matchBlock = document.getElementById("match-block");
const scoreCircle = document.getElementById("score-circle");
const scoreValue = document.getElementById("score-value");
const scoreLabel = document.getElementById("score-label");
const missingSkillsWrap = document.getElementById("missing-skills-wrap");
const missingSkillsList = document.getElementById("missing-skills-list");

let selectedFile = null;

// ---- File selection ----
dropzone.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", (e) => {
    if (e.target.files.length) handleFile(e.target.files[0]);
});

["dragenter", "dragover"].forEach(evt => {
    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        dropzone.classList.add("drag-over");
    });
});

["dragleave", "drop"].forEach(evt => {
    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        dropzone.classList.remove("drag-over");
    });
});

dropzone.addEventListener("drop", (e) => {
    if (e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]);
});

function handleFile(file) {
    const validExtensions = [".pdf", ".docx"];
    const isValid = validExtensions.some(ext => file.name.toLowerCase().endsWith(ext));

    if (!isValid) {
        setStatus("Unsupported file type. Please use PDF or DOCX.", true);
        return;
    }

    selectedFile = file;
    dropzone.classList.add("file-loaded");
    dropzoneText.textContent = file.name;
    analyzeBtn.disabled = false;
    setStatus("");
}

function setStatus(text, isError = false) {
    statusLine.textContent = text;
    statusLine.classList.toggle("error", isError);
}

// ---- Analyze ----
analyzeBtn.addEventListener("click", async () => {
    if (!selectedFile) return;

    analyzeBtn.disabled = true;
    setStatus("Analyzing resume...");

    const formData = new FormData();
    formData.append("resume", selectedFile);
    formData.append("job_description", jobDescriptionEl.value.trim());

    try {
        const res = await fetch("/api/analyze", {
            method: "POST",
            body: formData,
        });
        const data = await res.json();

        analyzeBtn.disabled = false;

        if (!res.ok) {
            setStatus(data.error || "Analysis failed. Please try again.", true);
            return;
        }

        setStatus("Analysis complete.");
        renderResults(data);

    } catch (err) {
        analyzeBtn.disabled = false;
        setStatus("Network error. Please try again.", true);
    }
});

function renderResults(data) {
    emptyState.style.display = "none";
    resultsContent.style.display = "block";

    // Candidate details
    detailGrid.innerHTML = "";
    const details = [
        { label: "Name", value: data.name },
        { label: "Email", value: data.email },
        { label: "Phone", value: data.phone },
        { label: "LinkedIn", value: data.links.linkedin ? `<a href="${data.links.linkedin}" target="_blank">View Profile</a>` : "Not found" },
    ];

    details.forEach(d => {
        const item = document.createElement("div");
        item.className = "detail-item";
        item.innerHTML = `
            <span class="detail-label">${d.label}</span>
            <span class="detail-value">${d.value}</span>
        `;
        detailGrid.appendChild(item);
    });

    // Skills
    skillsList.innerHTML = "";
    if (data.skills.length === 0) {
        skillsList.innerHTML = `<p class="no-data-text">No matching skills detected.</p>`;
    } else {
        data.skills.forEach((skill, i) => {
            const tag = document.createElement("span");
            tag.className = "skill-tag";
            tag.textContent = skill;
            tag.style.animationDelay = `${i * 0.03}s`;
            skillsList.appendChild(tag);
        });
    }

    // Education
    educationList.innerHTML = "";
    if (data.education.length === 0) {
        educationList.innerHTML = `<li class="no-data-text" style="border:none; background:none; padding:0;">No education details detected.</li>`;
    } else {
        data.education.forEach(line => {
            const li = document.createElement("li");
            li.textContent = line;
            educationList.appendChild(li);
        });
    }

    // Match score
    if (data.match_score !== null && data.match_score !== undefined) {
        matchBlock.style.display = "block";
        const score = data.match_score;

        scoreValue.textContent = `${score}%`;
        scoreCircle.style.background = `conic-gradient(var(--accent) ${score}%, var(--border) ${score}%)`;

        if (score >= 70) {
            scoreLabel.textContent = "Strong match with this job description.";
        } else if (score >= 40) {
            scoreLabel.textContent = "Moderate match — consider tailoring your resume further.";
        } else {
            scoreLabel.textContent = "Low match — this resume may need significant tailoring.";
        }

        missingSkillsList.innerHTML = "";
        if (data.missing_skills.length === 0) {
            missingSkillsWrap.style.display = "none";
        } else {
            missingSkillsWrap.style.display = "block";
            data.missing_skills.forEach(skill => {
                const tag = document.createElement("span");
                tag.className = "skill-tag missing";
                tag.textContent = skill;
                missingSkillsList.appendChild(tag);
            });
        }
    } else {
        matchBlock.style.display = "none";
    }
}

// ---- Theme toggle ----
const themeToggleBtn = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const themeLabel = document.getElementById("theme-label");

function applyTheme(theme) {
    if (theme === "dark") {
        document.documentElement.setAttribute("data-theme", "dark");
        themeIcon.textContent = "☀";
        themeLabel.textContent = "LIGHT";
    } else {
        document.documentElement.removeAttribute("data-theme");
        themeIcon.textContent = "🌙";
        themeLabel.textContent = "DARK";
    }
}

const savedTheme = localStorage.getItem("resumeiq-theme") || "light";
applyTheme(savedTheme);

themeToggleBtn.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
    const next = current === "dark" ? "light" : "dark";
    applyTheme(next);
    localStorage.setItem("resumeiq-theme", next);
});
