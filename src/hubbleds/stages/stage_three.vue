<template>
  <v-container>
    <v-row v-if="show_team_interface">
      <v-col>
        <v-btn
          color="error"
          class="black--text"
          @click="() => {
              console.log('stage state:', stage_state);
              console.log('story state:', story_state);
            }"
        >
          State
        </v-btn>
        Marker: {{ stage_state.marker }}
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
      v-if="stage_state.table_show.includes(stage_state.marker)"
    >
      <v-col
        cols="12"
        lg="5"
      >
        <c-guideline-explore-data
          v-if="stage_state.marker == 'exp_dat1'"
          v-intersect.once="scrollIntoView" />
        <v-btn
          block
        >PLACEHOLDER 1 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.table_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.table_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="widgets.fit_table"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
      v-if="stage_state.my_galaxies_plot_show.includes(stage_state.marker)"
    >
      <v-col
        cols="12"
        lg="5"
      >
        <c-guideline-trends-data-mc
          v-if="stage_state.marker == 'tre_dat1'"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.trend_response = true" />
        <c-guideline-trend-lines-draw
          v-if="stage_state.marker == 'tre_lin1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-best-fit-line
          v-if="stage_state.marker == 'bes_fit1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-relationship-vel-dist-mc
          v-if="stage_state.marker == 'rel_vel1'"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.relvel_response = true" />
        <c-guideline-hubbles-expanding-universe1
          v-if="stage_state.marker == 'hub_exp1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-hubbles-expanding-universe2
          v-if="stage_state.marker == 'hub_exp2' | stage_state.marker == 'run_rac1'"
          v-intersect.once="scrollIntoView" />       
        <c-slideshow-race
          v-if="stage_state.marker == 'run_rac1'"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.race_response = true" />
        <c-guideline-runners-vel-dist
          v-if="stage_state.marker == 'run_vel1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-age-universe
          v-if="stage_state.marker == 'age_uni1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-hypothetical-galaxy
          v-if="stage_state.marker == 'hyp_gal1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-age-race-equation
          v-if="stage_state.marker == 'age_rac1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-age-universe-equation
          v-if="stage_state.marker == 'age_uni2'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-age-universe-calc
          v-if="stage_state.marker == 'age_uni3'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-your-age-estimate
          v-if="stage_state.marker == 'you_age1'"
          v-intersect.once="scrollIntoView" />
        <c-guideline-shortcomings-reflect
          v-if="stage_state.marker == 'sho_ref1'"
          v-intersect.once="scrollIntoView" />
        <v-btn
          block
        >PLACEHOLDER 2 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.my_galaxies_plot_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.my_galaxies_plot_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.layer_viewer"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
    <!--
      v-if="stage_state.all_galaxies_plot_show.includes(stage_state.marker)"
    > 
    -->
      <v-col
        cols="12"
        lg="5"
      >
        <v-btn
          block
        >PLACEHOLDER 3 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.all_galaxies_plot_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.all_galaxies_plot_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.comparison_viewer"/>
          <c-student-slider />
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
    <!--
      v-if="stage_state.my_class_hist_show.includes(stage_state.marker)"
    >
    -->
      <v-col
        cols="12"
        lg="5"
      >
        <v-btn
          block
        >PLACEHOLDER 4 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.my_class_hist_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.my_class_hist_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.class_distr_viewer"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
    <!--
      v-if="stage_state.all_classes_hist_show.includes(stage_state.marker)"
    >
    -->
      <v-col
        cols="12"
        lg="5"
      >
        <v-btn
          block
        >PLACEHOLDER 5 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.all_classes_hist_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.all_classes_hist_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.all_distr_viewer"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
    <!--
      v-if="stage_state.sandbox_hist_show.includes(stage_state.marker)"
    >
    -->
      <v-col
        cols="12"
        lg="5"
      >
        <v-btn
          block
        >PLACEHOLDER 6 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.sandbox_hist_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.sandbox_hist_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.sandbox_distr_viewer"/>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
    <!--
      v-if="stage_state.all_galaxies_morph_plot_show.includes(stage_state.marker)"
    >
    -->
      <v-col
        cols="12"
        lg="5"
      >
        <v-btn
          block
        >PLACEHOLDER 7 {{ stage_state.marker }}</v-btn>
      </v-col>
      <v-col
        cols="12"
        lg="7"
      >
        <v-card
          :color="stage_state.all_galaxies_morph_plot_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.all_galaxies_morph_plot_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="viewers.morphology_viewer"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<style>

.v-alert .v-input--radio-group+.v-alert, .v-dialog .v-input--radio-group+.v-alert {
  background-color: #000b !important;
}

.v-radio label.theme--dark{
  color: white !important;
}

.v-radio label.theme--light{
  color: black !important;
}

.v-dialog .theme--dark .v-card__text {
  color: white !important;
}

.v-dialog .theme--light .v-card__text {
  color: black !important;
}

</style>


<script>

module.exports = {
  mounted() {
    const config = { childList: true, subtree: true };
    const onMutation = (mutationList, observer) => {
      for (const mutation of mutationList) {
        if (mutation.type === 'childList') {
          const target = mutation.target;
          const viewerName = this.viewerName(target);
          if (viewerName !== null) {
            const resizeObserver = new ResizeObserver((entries) => {
              for (const entry of entries) {
                const pixelSize = entry.devicePixelContentBoxSize[0];
                const width = pixelSize.inlineSize;
                const nticks = Math.floor(width / 125);
                this.set_viewer_nticks({ nticks: nticks, axis: 'x', viewer: viewerName });
              }
            });
            resizeObserver.observe(target, { box: 'device-pixel-content-box' });
          }
        }
      }
    }
    const observer = new MutationObserver(onMutation);
    observer.observe(this.$el, config);
  },
  methods: {
    scrollIntoView: function(entries, observer, isIntersecting) {
      if (isIntersecting) {
        entries[0].target.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    },
    viewerName: function(node) {
      for (const key of Object.keys(this.viewers)) {
        if (node.classList.contains(key)) {
          return key;
        }
      }
      return null;
    }
  }
}

</script>
