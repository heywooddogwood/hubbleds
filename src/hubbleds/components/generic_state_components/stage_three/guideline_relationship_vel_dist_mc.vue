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
      Relationship Between Velocity and Distance
    </h3>
    <div
      class="mb-4"
    >
      <p>
        Based on the best-fit line for your data, how would you describe the general relationship between the velocities and distances for galaxies?
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>The trend is:</p>
        <mc-radiogroup
          :radio-options="[
            'The velocity of galaxies are generally the same across all distances.',
            'Galaxies that are at a greater distance from us tend to have a larger velocity.',
            'Galaxies that are at a greater distance from us tend to have a smaller velocity.',
            'The velocity of galaxies appears to be random across all distances.'
          ]"
          :feedbacks="[
            'Recorded. You think velocity of galaxies are generally the same across all distances.',
            'Recorded. You think galaxies that are at a greater distance from us tend to have a larger velocity.',
            'Recorded. You think galaxies that are at a greater distance from us tend to have a smaller velocity.',
            'Recorded. You think the velocity of galaxies appears to be random across all distances.'
          ]"
          :correct-answers="[1]"
          :neutral-answers='[0,2,3]'
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
            state.marker = 'bes_fit1'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.relvel_response"
      >
        <div
          style="font-size: 16px;"
        >
          Answer the question above.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.relvel_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'hub_exp1'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
