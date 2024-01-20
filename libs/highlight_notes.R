library(dplyr)

# Function to highlight notes in the guitar chords data frame
highlight_notes <- function(root_note, intervals, guitar_chords_df, note_number_values) {

  # Add the selected number to each element of the notes list
  note_numbers <- lapply(intervals, function(x) x + root_note)  

  # Function to get note by index
  get_note_by_index <- function(index) {
    # Adjusting index to handle circular nature of notes
    adjusted_index <- (index %% length(note_number_value$Note)) + 1
    return(note_number_value$Note[adjusted_index])
  }

  # Apply function to a list of notes using sapply
  note_names <- sapply(note_numbers, get_note_by_index)

  # Function to replace values not in notes with NA
  replace_with_na <- function(x) {
    ifelse(x %in% note_names, x, NA)
  }
  
  # Apply the function to all columns of the dataframe
  df %>% mutate(across(everything(), replace_with_na))
  return(df)
}
