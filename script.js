// This object stores your answers as you click buttons.
// It ends up looking like: { q1: "cat", q2: "dog" }
const answers = {};

// Grab every option button on the page.
const optionButtons = document.querySelectorAll('.option-btn');

optionButtons.forEach((btn) => {
  btn.addEventListener('click', () => {
    const questionId = btn.dataset.questionId;
    const tag = btn.dataset.tag;

    // Remove "selected" from other buttons in the same question,
    // so only one option per question looks picked.
    document
      .querySelectorAll(`.option-btn[data-question-id="${questionId}"]`)
      .forEach((sibling) => sibling.classList.remove('selected'));

    btn.classList.add('selected');

    // Save this answer.
    answers[questionId] = tag;
  });
});

// When "See result" is clicked, send all answers to Flask.
/*document.getElementById('submitBtn').addEventListener('click', async () => {
  const res = await fetch('/score', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(answers)
  });

  const data = await res.json();
  document.getElementById('resultText').textContent = "Your result: " + data.result;
});*/

submitBtn.addEventListener('click', async () => {
  submitBtn.disabled = true;
  submitBtn.textContent = 'Calculating…';

  const res = await fetch('/score', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(answers)
  });
  const data = await res.json();

  document.getElementById('resultText').textContent = "Your result: " + data.emoji;
  document.getElementById('resultTitle').textContent = data.title;
  document.getElementById('resultDescription').textContent = data.description;
  document.getElementById('resultOverlay').hidden = false;
});

