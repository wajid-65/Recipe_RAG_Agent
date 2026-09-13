document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const userMessageInput = document.getElementById('userMessage');
    const chatMessages = document.getElementById('chatMessages');
    const welcomeBox = document.getElementById('welcomeBox');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const newChatBtn = document.getElementById('newChatBtn');
    const clearChatBtn = document.getElementById('clearChatBtn');
    const queryBtns = document.querySelectorAll('.query-btn');

    // Generate or load Session ID for conversational memory
    let sessionId = sessionStorage.getItem('recipe_rag_session_id');
    if (!sessionId) {
        sessionId = 'session_' + Math.random().toString(36).substring(2, 9) + '_' + Date.now();
        sessionStorage.setItem('recipe_rag_session_id', sessionId);
    }

    // Popular queries click handler
    queryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const query = btn.getAttribute('data-query');
            if (query) {
                userMessageInput.value = query;
                sendMessage(query);
            }
        });
    });

    // New Conversation
    newChatBtn.addEventListener('click', () => {
        sessionId = 'session_' + Math.random().toString(36).substring(2, 9) + '_' + Date.now();
        sessionStorage.setItem('recipe_rag_session_id', sessionId);
        chatMessages.innerHTML = '';
        if (welcomeBox) {
            chatMessages.appendChild(welcomeBox);
            welcomeBox.style.display = 'block';
        }
    });

    // Clear Chat UI
    clearChatBtn.addEventListener('click', () => {
        chatMessages.innerHTML = '';
        if (welcomeBox) {
            chatMessages.appendChild(welcomeBox);
            welcomeBox.style.display = 'block';
        }
    });

    // Form submission
    chatForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const text = userMessageInput.value.trim();
        if (text) {
            sendMessage(text);
        }
    });

    async function sendMessage(text) {
        if (welcomeBox) {
            welcomeBox.style.display = 'none';
        }

        appendUserMessage(text);
        userMessageInput.value = '';

        showLoading(true);

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: text,
                    session_id: sessionId
                })
            });

            const data = await response.json();
            showLoading(false);

            if (!response.ok) {
                appendBotMessage(`Error: ${data.detail || 'Failed to process query.'}`);
            } else {
                appendBotMessage(data.answer, text);
            }
        } catch (err) {
            showLoading(false);
            appendBotMessage(`Network Error: Could not connect to server. (${err.message})`);
        }
    }

    function showLoading(show) {
        if (show) {
            loadingIndicator.classList.remove('hidden');
            chatMessages.appendChild(loadingIndicator);
            scrollToBottom();
        } else {
            loadingIndicator.classList.add('hidden');
        }
    }

    function appendUserMessage(text) {
        const row = document.createElement('div');
        row.className = 'message-row user';

        const label = document.createElement('div');
        label.className = 'sender-label';
        label.textContent = 'You';

        const bubble = document.createElement('div');
        bubble.className = 'message-bubble';
        bubble.textContent = text;

        row.appendChild(label);
        row.appendChild(bubble);
        chatMessages.appendChild(row);
        scrollToBottom();
    }

    function appendBotMessage(text, originalPrompt = '') {
        const row = document.createElement('div');
        row.className = 'message-row bot';

        const label = document.createElement('div');
        label.className = 'sender-label';
        label.textContent = 'Recipe Assistant';

        const bubble = document.createElement('div');
        bubble.className = 'message-bubble';

        if (typeof marked !== 'undefined' && typeof marked.parse === 'function') {
            bubble.innerHTML = marked.parse(text);
        } else {
            bubble.textContent = text;
        }

        row.appendChild(label);
        row.appendChild(bubble);

        // Add Follow-up Questions Suggestions
        const followups = getFollowUpSuggestions(text, originalPrompt);
        if (followups && followups.length > 0) {
            const followupContainer = document.createElement('div');
            followupContainer.className = 'followup-container';

            followups.forEach(suggestionText => {
                const chip = document.createElement('button');
                chip.className = 'followup-chip';
                chip.textContent = suggestionText;
                chip.addEventListener('click', () => {
                    userMessageInput.value = suggestionText;
                    sendMessage(suggestionText);
                });
                followupContainer.appendChild(chip);
            });

            row.appendChild(followupContainer);
        }

        chatMessages.appendChild(row);
        scrollToBottom();
    }

    function getFollowUpSuggestions(answerText, promptText) {
        const lowerAnswer = answerText.toLowerCase();
        const lowerPrompt = promptText.toLowerCase();
        const suggestions = [];

        if (lowerAnswer.includes('recipe name') || lowerAnswer.includes('ingredients:')) {
            if (!lowerPrompt.includes('vegan') && !lowerPrompt.includes('vegetarian')) {
                suggestions.push('🌱 How do I make this vegan/vegetarian?');
            }
            if (!lowerPrompt.includes('gluten')) {
                suggestions.push('🌾 Is there a gluten-free substitution?');
            }
            if (!lowerPrompt.includes('shopping list')) {
                suggestions.push('🛒 Give me the shopping list for this');
            }
            if (!lowerPrompt.includes('nutrition') && !lowerPrompt.includes('calories')) {
                suggestions.push('📊 Show nutritional breakdown per serving');
            }
        } else {
            suggestions.push('💡 Show another recipe from this cuisine');
            suggestions.push('⏱️ Give me a recipe under 30 minutes');
            suggestions.push('🥗 Recommend a healthy high-protein meal');
        }

        return suggestions.slice(0, 3);
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
