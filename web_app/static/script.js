let currentInput = '';
let currentOperator = null;
let previousInput = null;

function appendNumber(num) {
    currentInput += num;
    document.getElementById('result').value = currentInput;
}

function setOperator(op) {
    if (op === 'add') op = 'add';
    else if (op === '/') op = 'divide';
    else if (op === '*') op = 'multiply';
    else if (op === '-') op = 'subtract';

    if (currentInput === '') return;
    if (previousInput !== null) {
        calculate();
    }
    previousInput = currentInput;
    currentInput = '';
    currentOperator = op;
}

function setOp(op) {
    if (currentInput === '') return;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: op,
            a: parseFloat(currentInput)
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.detail) {
            alert(data.detail);
        } else {
            currentInput = data.result.toString();
            document.getElementById('result').value = currentInput;
            previousInput = null;
            currentOperator = null;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function clearDisplay() {
    currentInput = '';
    previousInput = null;
    currentOperator = null;
    document.getElementById('result').value = '';
}

function calculate() {
    if (currentOperator === null || previousInput === null || currentInput === '') return;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: currentOperator,
            a: parseFloat(previousInput),
            b: parseFloat(currentInput)
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.detail) {
            alert(data.detail);
        } else {
            currentInput = data.result.toString();
            document.getElementById('result').value = currentInput;
            previousInput = null;
            currentOperator = null;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
