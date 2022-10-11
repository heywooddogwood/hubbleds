<template>
  <v-dialog
      v-model="state.race_dialog"
      persistent
      max-width="800px"
  >
    <v-card
      class="mx-auto race_dialog"
      color="info"
    >
      <v-card-text
        class="pt-8"
      >
        <h3
          class="mb-4"
        >
          A Running Race
        </h3>
        <div
          class="mb-4"
        >
          <p>
            To understand Hubble’s thinking about this, let’s use the following situation as a model: Imagine runners in the middle of a race, where the runners are running at different speeds.
          </p>
          <p>
            In this diagram, runner A is running with a velocity of 4 km per hour and has run a distance of 12 km, while runner C is running faster with a velocity of 10 km per hour and has gone a distance of 30 km.
          </p>
          <p>
            Can you figure out how long ago the race started — the “age” of the race? (Assume each runner has maintained a consistent speed for the entire race).
          </p>
          <v-container
            class="px-0"
            fluid
          >
            <p>The race began:</p>
            <v-radio-group>
              <v-radio
                key="1"
                label="1/3 of an hour ago"
                value="1"
              ></v-radio>
              <v-radio
                key="2"
                label="3 hours ago"
                value="2"
              ></v-radio>
              <v-radio
                key="3"
                label="12 hours ago"
                value="3"
              ></v-radio>
              <v-radio
                key="4"
                label="75 hours ago"
                value="4"
              ></v-radio>
            </v-radio-group>
          </v-container>
        </div>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn
          color="accent"
          class="black--text"
          depressed
          @click="() => {
            state.race_dialog = false;
            state.marker = 'hub_exp2'
          }"
        >
          Back
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn
          color="accent"
          class="black--text"
          depressed
          @click="() => { 
            $emit('submit'); 
            state.race_dialog = false;
            state.marker = 'run_vel1'
          }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<style>
      
.v-card.race_dialog .v-card__text{
  font-size: 18px !important;
}

.v-card.race_dialog.theme--dark  .v-card__text{
  color: #fff;
}

</style>


<script>
export default = {
  methods: {
  },
  watch: {
  }
};
</script>
