<template>
  <scaffold-alert
    header-text="Age of the Race"
    @back="
      state.marker = 'hyp_gal1';
    "
    @next="
      state.marker = 'age_uni2';
    "
  >
    <div
      class="mb-4"
      v-intersect="(entries, _observer, intersecting) => { if (intersecting) { MathJax.typesetPromise(entries.map(entry => entry.target)) }}"
    >
      <p>
        Recall from our runners, that the "age" of the runners' race can be found from:
      </p>
      <v-card
        outlined
        class="legend mt-8"
        color="info"
      >
        <v-container>
          <v-row
            no-gutters
          >
            <v-col>
              <div
                class="JaxEquation mx-auto"
              >
                $$ t = \frac{d}{v} $$
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(t\)
            </v-col>
            <v-col
              cols="10"
            >
              time that has passed (age of the race)
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(d\)
            </v-col>
            <v-col
              cols="10"
            >
              distance the runner has run
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(v\)
            </v-col>
            <v-col
              cols="10"
            >
              velocity of the runner
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
  </scaffold-alert>
</template>
