async function calculateGPA() {
    const input = document.getElementById('grades-input').value;
    if (!input.trim()) {
        alert("Please enter grades.");
        return;
    }

    try {
        const grades = input.split(',').map(grade => parseFloat(grade.trim())).filter(g => !isNaN(g));
        if (grades.length === 0) {
            alert("Please enter valid numbers");
            return;
        }

        const response = await fetch('/api/calculate_gpa', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ grades: grades })
        });

        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('gpa-value').textContent = data.gpa;
            document.getElementById('gpa-result').classList.remove('hidden');
        } else {
            alert("Error: " + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to calculate GPA.');
    }
}

async function predictGrade() {
    const studyHours = document.getElementById('study-hours').value;
    const prevGpa = document.getElementById('prev-gpa').value;

    if (!studyHours || !prevGpa) {
        alert("Please fill out both fields.");
        return;
    }

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                study_hours: parseFloat(studyHours),
                previous_gpa: parseFloat(prevGpa)
            })
        });

        const data = await response.json();

        if (data.status === 'success') {
            document.getElementById('prediction-value').textContent = data.predicted_grade;
            document.getElementById('prediction-result').classList.remove('hidden');
        } else {
            alert("Error: " + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to predict grade.');
    }
}
