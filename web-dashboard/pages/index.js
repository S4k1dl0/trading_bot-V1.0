import React, { useState } from 'react';

export default function Home() {
    const [result, setResult] = useState(null);

    const testStrategy = async () => {
        const res = await fetch("http://localhost:5000/strategy", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                rsi: 30,
                dca: 3,
                grid: { lower: 68000, upper: 70000, step: 500 },
                macd: true,
                ml: true
            })
        });
        const json = await res.json();
        setResult(json);
    };

    return (
        <div>
            <h1>Trading Bot Dashboard</h1>
            <button onClick={testStrategy}>Test Strategy</button>
            {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
        </div>
    );
}
