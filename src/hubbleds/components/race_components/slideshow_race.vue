<template>
  <v-dialog
      v-model="state.race_dialog"
      persistent
      max-width="1000px"
  >
    <v-card
      class="mx-auto race_dialog"
      color="info"
    >
      <v-card-text
        style="height: 70vh;"
        class="pt-8 overflow-auto"
      >
        <h3
          class="mb-4"
        >
          A Running Race
        </h3>
        <div
          class="mb-4"
        >
          <v-container
            class="px-0"
            fluid
          >
            <v-row>
              <v-col
                cols="8"
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
              </v-col>
              <v-col
                cols="4"
              >
                <v-alert
                  class="text-center"
                  min-height="200px"
                >
                  place picture here
                </v-alert>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                col="12"
              >
                <p>The race began:</p>
                <mc-radiogroup
                  :radio-options="[
                    '1/3 of an hour ago.',
                    '3 hours ago.',
                    '12 hours ago.',
                    '75 hours ago.'
                  ]"
                  :feedbacks="[
                    'Recorded. You think the race began 1/3 of an hour ago.',
                    'Recorded. You think the race began 3 hours ago.',
                    'Recorded. You think the race began 12 hours ago.',
                    'Recorded. You think the race began 75 hours ago.'
                  ]"
                  :correct-answers="[1]"
                  :neutral-answers='[0,2,3]'
                  :selected-callback="(state) => { $emit('ready'); }"
                >
                </mc-radiogroup>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn
          color="accent"
          class="black--text"
          @click="() => {
            state.race_dialog = false;
            state.marker = 'hub_exp2'
          }"
        >
          Back
        </v-btn>

        <v-spacer></v-spacer>

        <v-col
        cols="6"
        class="shrink"
        v-if="!state.race_response"
        >
          <div
            style="font-size: 16px;"
          >
            Answer the question above.
          </div>
        </v-col>
        <v-col
          class="shrink"
          v-if="state.race_response"
        >
          <v-btn
            color="accent"
            class="black--text"
            @click="() => { 
              $emit('submit'); 
              state.race_dialog = false;
              state.marker = 'run_vel1'
            }"
          >
            Done
          </v-btn>
        </v-col>
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
