
'use client';

import { useState } from 'react';

// A simple component to display a single chat message
const ChatMessage = ({ text, sender }: { text: string; sender: 'user' | 'bot' }) => {
  const alignment = sender === 'user' ? 'text-right' : 'text-left';
  const bgColor = sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black';
  return (
    <div className={`p-2 my-2 rounded-lg ${bgColor} ${alignment}`}>
      <p>{text}</p>
    </div>
  );
};

export default function ChatPage() {
  const [messages, setMessages] = useState([
    { text: 'سلام! من یک چت‌بات هوشمند برای پژوهشگران هستم. چطور می‌توانم به شما کمک کنم؟', sender: 'bot' }
  ]);
  const [inputText, setInputText] = useState('');

  const handleSendMessage = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim()) return;

    // Add user message to the chat
    setMessages([...messages, { text: inputText, sender: 'user' }]);
    setInputText('');

    // TODO: Send message to the backend and get a response
  };

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold text-center mb-4">چت با دستیار هوشمند</h1>

      {/* Message display area */}
      <div className="flex-grow overflow-y-auto border p-4 rounded-lg">
        {messages.map((msg, index) => (
          <ChatMessage key={index} text={msg.text} sender={msg.sender} />
        ))}
      </div>

      {/* Message input form */}
      <form onSubmit={handleSendMessage} className="mt-4 flex">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="پیام خود را بنویسید..."
          className="flex-grow px-3 py-2 bg-white border border-gray-300 rounded-l-md shadow-sm text-black focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
        />
        <button
          type="submit"
          className="px-4 py-2 border border-transparent rounded-r-md shadow-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none"
        >
          ارسال
        </button>
      </form>
    </div>
  );
}
