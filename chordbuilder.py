import streamlit as st
import pandas as pd

# Load CSV files
@st.cache_data
def load_data():
    guitar_chords_df = pd.read_csv("guitar_chords_df.csv")
    note_number_value = pd.read_csv("note_number_value.csv")
    progression_number_value = pd.read_csv("progression_number_value.csv")
    return guitar_chords_df, note_number_value, progression_number_value

guitar_chords_df, note_number_value, progression_number_value = load_data()

# Function to select chord
def select_chord(selected_note, note_number, intervals):
    mask = guitar_chords_df.isin([selected_note] + note_number_value['Note'][note_number + pd.Series(intervals)].tolist())
    return guitar_chords_df.where(mask, ' ')

# Function to get progression notes
def get_progression_notes(selected_note_number, progression_numbers):
    progression_notes = []
    for interval in progression_numbers:
        note_to_add = progression_number_value.loc[progression_number_value['Number'] == (selected_note_number + interval), 'Note'].values
        if len(note_to_add) > 0:
            progression_notes.append(note_to_add[0])
        else:
            progression_notes.append("N/A")
    return progression_notes

# Define chord intervals
chord_intervals = {
    "Major": [4, 7],
    "Minor": [3, 7],
    "Diminished": [3, 6],
    "maj7": [4, 7, 11],
    "Dominant 7": [4, 7, 10],
    "min7": [3, 7, 10],
    "sus2": [2, 7],
    "sus4": [5, 7],
    "add2": [2, 4, 7],
    "madd2": [2, 3, 7],
    "5th": [7],
    "6th": [4, 7, 9],
    "min6": [3, 7, 9],
    "mM7": [3, 7, 11],
    "9th": [2, 4, 7, 10],
    "min9": [2, 3, 10],
    "maj9": [2, 4, 10],
    "Dominant 9": [2, 4, 11],
    "dim7": [3, 6, 9],
    "1/2 dim7": [3, 6, 10],
    "aug M7": [4, 8, 11],
    "aug 7": [4, 8, 10],
    "7sus4": [5, 7, 10],
    "9sus4": [2, 5, 7, 10],
    "add9": [2, 4, 7],
    "madd9": [2, 3, 7]
}

# Define progression intervals
progression_intervals = {
    1: {"name": "I V ii IV", "intervals": [0, 14, 3, 10], "song": ""},
    2: {"name": "ii V I", "intervals": [23, 10, 20], "song": "'Sunday Morning' by Maroon 5"},
    3: {"name": "I vi IV V", "intervals": [0, 17, 10, 14], "song": "'In the Aeroplane Over the Sea' by Neutral Milk Hotel"},
    4: {"name": "I V vi IV", "intervals": [0, 14, 17, 10], "song": "'Let it Be' by The Beatles"},
    5: {"name": "I IV V", "intervals": [0, 10, 14], "song": "'Good Riddance' by Green Day"},
    6: {"name": "vi IV I V", "intervals": [23, 16, 6, 20], "song": "'Apologize' by OneRepublic"},
    7: {"name": "I IV vi V", "intervals": [0, 10, 17, 14], "song": "'Say' by John Mayer"},
    8: {"name": "vi ii V I", "intervals": [23, 9, 20, 6], "song": "'Island in the Sun' by Weezer"},
    9: {"name": "I III IV iv", "intervals": [0, 8, 10, 9], "song": "'Creep' by Radiohead"},
    10: {"name": "I V vi iii IV I IV V", "intervals": [0, 14, 17, 7, 10, 0, 10, 14], "song": "'Canon in D' by Pachelbel"},
    11: {"name": "VI IV ii", "intervals": [0, 16, 9], "song": "'Oh Comely' by Neutral Milk Hotel"},
    12: {"name": "i VI III VII", "intervals": [23, 18, 8, 20], "song": "'Faded' by Alan Walker"},
    13: {"name": "i III VII VI", "intervals": [23, 8, 20, 18], "song": "'Levels' by Avicii"},
    14: {"name": "i iii7 vi IV", "intervals": [23, 8, 17, 10], "song": "'Heroes' by Alesso"},
    15: {"name": "i7 III v7 IV", "intervals": [23, 8, 13, 10], "song": "'Get Lucky' by Daft Punk"},
    16: {"name": "I IV ii V", "intervals": [0, 10, 3, 14], "song": ""},
    17: {"name": "I vi ii V", "intervals": [0, 9, 3, 14], "song": ""},
    18: {"name": "ii bII7 I", "intervals": [23, 22, 19], "song": "- 2nd Chord is a Dominant 7"},
    19: {"name": "ii bIII I", "intervals": [23, 2, 19], "song": ""},
    20: {"name": "IVM7 V7 iii7 vi", "intervals": [0, 4, 7, 9], "song": "- 1st Chord is maj7, 2nd is dom7, 3rd is dom7"}
}

# Apply custom CSS for styling
def local_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #F7F9F9;
        }
        .sidebar .sidebar-content {
            background-color: #D5F5E3;
        }
        .progression-text {
            font-size: 20px;
        }
        h1 {
            text-align: center;
            font-size: 24px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

local_css()

# Title of the app
st.title("Guitar Chord Builder")

# Sidebar for inputs
with st.sidebar:
    st.markdown("<div style='background-color: #D5F5E3; padding: 10px; border-radius: 5px;'></div>", unsafe_allow_html=True)
    selected_note = st.text_input("Enter a Note for Chord Builder (e.g., C):", "")
    submit_btn = st.button("Submit")
    choose_chord_type = st.selectbox(
        "Select Chord Type",
        options=[
            "Major", "Minor", "Diminished", "maj7", "Dominant 7", "min7", "sus2", "sus4",
            "add2", "madd2", "5th", "6th", "min6", "mM7", "9th", "min9", "maj9",
            "Dominant 9", "dim7", "1/2 dim7", "aug M7", "aug 7", "7sus4", "9sus4",
            "add9", "madd9"
        ],
        index=0
    )
    selected_chord = st.text_input("Enter a Chord for Progressions (e.g., G):", "")
    submit_prog_btn = st.button("Submit Progression")

# Initialize session state for chord shape
if 'chord_shape' not in st.session_state:
    st.session_state.chord_shape = guitar_chords_df.copy()

# Handle chord submission
if submit_btn and selected_note:
    # Get the lowest number value of the selected note
    note_numbers = note_number_value.loc[note_number_value['Note'] == selected_note, 'Number']
    if not note_numbers.empty:
        note_number = note_numbers.min()
        intervals = chord_intervals.get(choose_chord_type, [])
        st.session_state.chord_shape = select_chord(selected_note, note_number, intervals)
        st.success(f"Selected Note: {selected_note}, Chord Type: {choose_chord_type}")
    else:
        st.error("Selected note not found in note_number_value.csv")

# Tabs for Chord Builder and Chord Progressions
tab1, tab2 = st.tabs(["Chord Builder", "Chord Progressions"])

with tab1:
    st.table(st.session_state.chord_shape)
    if selected_note and submit_btn:
        st.markdown(f"**Chord Shown:** {selected_note} **Chord Type:** {choose_chord_type}")

with tab2:
    if submit_prog_btn and selected_chord:
        # Find the minimum number associated with the selected note
        prog_note_numbers = progression_number_value.loc[progression_number_value['Note'] == selected_chord, 'Number']
        if not prog_note_numbers.empty:
            selected_note_number = prog_note_numbers.min()
            # Display all progression texts
            for i in range(1, 21):
                progression = progression_intervals.get(i, {})
                if progression:
                    progression_notes = get_progression_notes(selected_note_number, progression["intervals"])
                    progression_text = f"{progression['name']}: {' - '.join(progression_notes)}"
                    if progression["song"]:
                        progression_text += f" {progression['song']}"
                    st.markdown(f"### {progression_text}", unsafe_allow_html=False)
        else:
            st.error("Selected chord not found in progression_number_value.csv")
    else:
        st.write("Enter a chord and click 'Submit Progression' to see chord progressions.")

# ### New Line: Displaying Text at the Bottom of the Page ###
# You can use `st.markdown` or `st.write` to display text. Here's an example:
st.markdown("---")  # Adds a horizontal line for separation
st.write("Enter a note in the 1st entry space, and a note shape in the dropdown, to view chord shapes for that note on the 1st page. Enter a chord in the 2nd entry space to view progressions for that chord on the 2nd page.")  # Replace with your desired text


