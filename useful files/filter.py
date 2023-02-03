import streamlit as st
import numpy as np
import pandas as pd

# 4 filter example that can be useful


def call_filters(df, i):
    selected_filters = []
    with st.expander("Filter Türkiye data only for this question"):
        age, stage = st.columns(2)

        with age:
            age_list = ['1', '2', '3', '4', '5', '6', '7', '8',
                        '9', '10', '11-15', '16-20', '20+', np.nan]
            age = st.container()
            keyname = str(i) + "_age"
            all_age = st.checkbox("Select all", value=True, key=keyname)
            if all_age:
                age.markdown("Instutional Age:")
                age.markdown("All age categories are selected.")
                selected_ages = age_list
            else:
                selected = age.multiselect(
                    "Instutional Age:", [item for item in age_list if not (pd.isnull(item)) == True], key=keyname)
                if len(selected) == 0:
                    selected_ages = age_list
                else:
                    selected_ages = selected
            selected_filters.append(selected_ages)

        with stage:
            stage_list = list(df.stage.unique())
            stage = st.container()
            keyname = str(i) + "_stage"
            all_stage = st.checkbox("Select all", value=True, key=keyname)
            if all_stage:
                stage.markdown("Stage of Development:")
                stage.markdown("All stage categories are selected.")
                selected_stages = stage_list
            else:
                selected = stage.multiselect(
                    "Stage of Development:", stage_list, key=keyname)
                if len(selected) == 0:
                    selected_stages = stage_list
                else:
                    selected_stages = selected
            selected_filters.append(selected_stages)
        legal, sector = st.columns(2)

        with legal:
            legal_form_list = list(df.legal_form.unique())
            legal_form = st.container()
            keyname = str(i) + "_legal"
            all_legal = st.checkbox("Select all", value=True, key=keyname)
            if all_legal:
                legal_form.markdown("Legal Form:")
                legal_form.markdown("All legal form categories are selected.")
                selected_forms = legal_form_list
            else:
                selected = legal_form.multiselect(
                    "Legal Form:", legal_form_list, key=keyname)
                if len(selected) == 0:
                    selected_forms = legal_form_list
                else:
                    selected_forms = selected
            selected_filters.append(selected_forms)

        with sector:
            sector_list = list(df.sector.unique())
            sector = st.container()
            keyname = str(i) + "_sector"
            all_sector = st.checkbox(
                "Select all", value=True, key=keyname)
            if all_sector:
                sector.markdown("Sector:")
                sector.markdown("All sector categories are selected.")
                selected_sectors = sector_list
            else:
                selected = sector.multiselect(
                    "Sector:", sector_list, key=keyname)
                if len(selected) == 0:
                    selected_sectors = sector_list
                else:
                    selected_sectors = selected
            selected_filters.append(selected_sectors)
    return selected_filters
