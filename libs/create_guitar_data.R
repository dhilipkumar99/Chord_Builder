###### Create our chord dataframe

create_guitar_data <- function() {
    create_guitar_chords_df <- function(){
        guitar_chords <- list(
        c("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"),
        c("B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"),
        c("G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"),
        c("D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"),
        c("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"),
        c("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E")
        )

        # Convert the list to a dataframe
        guitar_chords_df <- as.data.frame(do.call(rbind, guitar_chords))

        return(guitar_chords_df)
    }
    guitar_chords_df <- create_guitar_chords_df()

    # Assign notes a number value
    note_number_values <- data.frame(
        Note = c("G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"),
        Number = 0:12
    )
    return(list(guitar_chords_df = guitar_chords_df, note_number_values = note_number_values))
}