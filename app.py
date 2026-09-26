import streamlit as st
import pandas as pd

st.title("Interaktiv dataanalys med Streamlit")

uploaded_file = st.file_uploader("Ladda upp en CSV-fil", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Förhandsvisning av data")
        st.dataframe(df.head())

        st.write("Antal rader:", df.shape[0])
        st.write("Antal kolumner:", df.shape[1])

        st.write("Kolumner:")
        st.write(list(df.columns))

        st.write("Datatyper:")
        st.write(df.dtypes)

        st.write("Saknade värden:")
        st.write(df.isnull().sum())

        st.subheader("Statistisk sammanfattning")
        st.dataframe(df.describe())

        st.write("Välj en kolumn:")
        selected_column = st.selectbox("Kolumn", df.columns)

        st.write("Vald kolumn:")
        st.write(df[selected_column])

        if pd.api.types.is_numeric_dtype(df[selected_column]):
            chart_type = st.selectbox(
                "Välj diagramtyp",
                ["Stapeldiagram", "Linjediagram"]
            )

            if chart_type == "Stapeldiagram":
                st.bar_chart(df[selected_column])

            elif chart_type == "Linjediagram":
                st.line_chart(df[selected_column])

            st.write("Medelvärde:")
            st.write(df[selected_column].mean())

            st.write("Minsta värde:")
            st.write(df[selected_column].min())

            st.write("Största värde:")
            st.write(df[selected_column].max())

        else:
            st.info(
                "Den valda kolumnen är inte numerisk och kan därför inte visualiseras med dessa diagram."
            )

    except Exception:
        st.error(
            "Filen kunde inte läsas. Kontrollera att det är en giltig CSV-fil."
        )
        