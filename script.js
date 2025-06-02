const story = [
    "You take a step closer to the mirror. The air feels colder.",
    "Your reflection seems to lag behind your movements.",
    "A shadow flickers in the glass, but vanishes when you blink.",
    "You hear a faint whisper: 'Why did you come here?'",
    "The mirror fogs up, and a handprint appears from the other side.",
    "Your reflection smiles, but you do not.",
    "Suddenly, the lights flicker. For a moment, you see someone standing behind you.",
    "The mirror starts to crack, and a scream echoes through the room.",
    "Everything goes black. You feel cold hands pulling you into the glass...",
    "THE END."
];
let step = 0;

document.getElementById("next").addEventListener("click", function() {
    if (step < story.length) {
        document.getElementById("story").innerText = story[step];
        step++;
        if (step === story.length) {
            this.style.display = "none";
        }
    }
});
