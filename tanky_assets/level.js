// levels.js - exported array of levels
const levels = [
    { enemies: [{x:180,y:-200}], theme: 'flat', baseScore: 100 },
    { enemies: [{x:220,y:-200}, {x:320,y:-200}], theme: 'flat', baseScore: 150 },
    { enemies: [{x:180,y:-200}, {x:320,y:-280}, {x:420,y:-200}], theme: 'flat', baseScore: 200 },
    { enemies: [{x:150,y:-180}, {x:280,y:-280}, {x:380,y:-150}, {x:500,y:-250}], theme: 'flat', baseScore: 250 },
    { enemies: [{x:120,y:-200}, {x:250,y:-300}, {x:380,y:-180}, {x:480,y:-260}, {x:550,y:-140}], theme: 'flat', baseScore: 300 },
    { enemies: [{x:200,y:-150}, {x:300,y:-100}, {x:400,y:-150}], theme: 'hilly', baseScore: 350 },
    { enemies: [{x:180,y:-250}, {x:280,y:-180}, {x:380,y:-250}, {x:480,y:-180}], theme: 'hilly', baseScore: 400 },
    { enemies: [{x:220,y:-300}, {x:320,y:-220}, {x:420,y:-300}, {x:520,y:-220}], theme: 'hilly', baseScore: 450 },
    { enemies: [{x:150,y:-120}, {x:250,y:-280}, {x:350,y:-120}, {x:450,y:-280}, {x:550,y:-120}], theme: 'hilly', baseScore: 500 },
    { enemies: [{x:200,y:-100}, {x:300,y:-250}, {x:400,y:-100}, {x:500,y:-250}, {x:600,y:-100}], theme: 'hilly', baseScore: 550 },
    { enemies: [{x:250,y:-180}, {x:280,y:-180}, {x:310,y:-180}], theme: 'cluster', baseScore: 600 },
    { enemies: [{x:300,y:-250}, {x:350,y:-200}, {x:400,y:-250}], theme: 'cluster', baseScore: 650 },
    { enemies: [{x:200,y:-300}, {x:250,y:-250}, {x:300,y:-300}, {x:350,y:-250}, {x:400,y:-300}], theme: 'cluster', baseScore: 700 },
    { enemies: [{x:180,y:-220}, {x:230,y:-220}, {x:280,y:-220}, {x:330,y:-220}, {x:380,y:-220}], theme: 'cluster', baseScore: 750 },
    { enemies: [{x:250,y:-150}, {x:300,y:-200}, {x:350,y:-150}, {x:300,y:-100}], theme: 'cluster', baseScore: 800 },
    { enemies: [{x:220,y:-350}, {x:320,y:-300}, {x:420,y:-350}], theme: 'defended', baseScore: 900 },
    { enemies: [{x:200,y:-380}, {x:300,y:-320}, {x:400,y:-380}, {x:500,y:-340}], theme: 'defended', baseScore: 950 },
    { enemies: [{x:180,y:-400}, {x:260,y:-360}, {x:340,y:-360}, {x:420,y:-400}, {x:500,y:-380}], theme: 'defended', baseScore: 1000 },
    { enemies: [{x:150,y:-420}, {x:240,y:-380}, {x:330,y:-360}, {x:420,y:-380}, {x:510,y:-420}], theme: 'defended', baseScore: 1050 },
    { enemies: [{x:200,y:-450}, {x:280,y:-410}, {x:360,y:-370}, {x:440,y:-410}, {x:520,y:-450}], theme: 'defended', baseScore: 1100 },
    { enemies: [{x:180,y:-380}, {x:240,y:-340}, {x:300,y:-360}, {x:360,y:-340}, {x:420,y:-380}, {x:480,y:-360}], theme: 'expert', baseScore: 1200 },
    { enemies: [{x:200,y:-400}, {x:260,y:-370}, {x:320,y:-340}, {x:380,y:-370}, {x:440,y:-400}, {x:500,y:-370}], theme: 'expert', baseScore: 1250 },
    { enemies: [{x:220,y:-420}, {x:280,y:-390}, {x:340,y:-360}, {x:400,y:-390}, {x:460,y:-420}, {x:520,y:-390}, {x:580,y:-410}], theme: 'expert', baseScore: 1300 },
    { enemies: [{x:180,y:-440}, {x:240,y:-410}, {x:300,y:-380}, {x:360,y:-410}, {x:420,y:-440}, {x:480,y:-410}, {x:540,y:-390}], theme: 'expert', baseScore: 1350 },
    { enemies: [{x:200,y:-460}, {x:260,y:-430}, {x:320,y:-400}, {x:380,y:-430}, {x:440,y:-460}, {x:500,y:-430}, {x:560,y:-410}, {x:620,y:-440}], theme: 'expert', baseScore: 1400 }
];

// Make it globally available so the game can use it
window.levels = levels;
