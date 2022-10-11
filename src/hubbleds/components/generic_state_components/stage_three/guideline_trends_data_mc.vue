<template>
  <v-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
  >
    <h3
      class="mb-4"
    >
      Trends in the Data
    </h3>
    <div
      class="mb-4"
    >
      <p>
        Do you see any sort of trend in your data? Is there a relationship between the velocity and distance of the galaxy?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Yes, I see a trend.',
            'No, I don\'t see a trend.',
            'I can\'t tell if there\'s a trend.',
            'What\'s a trend??'
          ]"
          :feedbacks="[
            'Recorded. You see a trend.',
            'Recorded. You don\'t see a trend.',
            'Recorded. You can\'t tell if there\'s a trend.',
            'Recorded. You don\'t know what a trend is.'
          ]"
          :correct-answers="[]"
          :neutral-answers='[0,1,2,3]'
          :selected-callback="(state) => { $emit('ready'); }"
        >
        </mc-radiogroup>
      </v-container>
    </div>
    
    <v-divider
      class="my-4"
    >
    </v-divider>

    <v-row
      align="center"
      no-gutters
    >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'exp_dat1'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.trend_response"
      >
        <div
          style="font-size: 16px;"
        >
          Answer the question above.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.trend_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'tre_lin1'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
